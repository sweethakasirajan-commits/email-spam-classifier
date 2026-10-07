from flask import Flask, render_template, request
import joblib
import os
import sqlite3
from datetime import datetime

app = Flask(__name__)

# -------------------------------------------------
# PATHS
# -------------------------------------------------

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

MODEL_PATH = os.path.join(
    BASE_DIR, "..", "model", "spam_model.pkl"
)

VECTORIZER_PATH = os.path.join(
    BASE_DIR, "..", "model", "tfidf_vectorizer.pkl"
)

DATABASE = os.path.join(BASE_DIR, "email_history.db")


# -------------------------------------------------
# LOAD MACHINE LEARNING MODEL
# -------------------------------------------------

model = joblib.load(MODEL_PATH)
vectorizer = joblib.load(VECTORIZER_PATH)


# -------------------------------------------------
# DATABASE
# -------------------------------------------------

def init_database():

    connection = sqlite3.connect(DATABASE)

    cursor = connection.cursor()

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS email_history (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            message TEXT NOT NULL,
            prediction TEXT NOT NULL,
            confidence REAL,
            analyzed_at TEXT NOT NULL
        )
    """)

    connection.commit()
    connection.close()


# -------------------------------------------------
# SAVE PREDICTION
# -------------------------------------------------

def save_prediction(message, prediction, confidence):

    connection = sqlite3.connect(DATABASE)

    cursor = connection.cursor()

    cursor.execute("""
        INSERT INTO email_history
        (message, prediction, confidence, analyzed_at)
        VALUES (?, ?, ?, ?)
    """, (
        message,
        prediction,
        confidence,
        datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    ))

    connection.commit()
    connection.close()


# -------------------------------------------------
# GET HISTORY
# -------------------------------------------------

def get_history():

    connection = sqlite3.connect(DATABASE)

    connection.row_factory = sqlite3.Row

    cursor = connection.cursor()

    cursor.execute("""
        SELECT *
        FROM email_history
        ORDER BY id DESC
        LIMIT 10
    """)

    history = cursor.fetchall()

    connection.close()

    return history


# -------------------------------------------------
# HOME PAGE
# -------------------------------------------------

@app.route("/", methods=["GET", "POST"])
def home():

    prediction = None
    confidence = None
    message = ""

    if request.method == "POST":

        message = request.form.get("message", "").strip()

        if message:

            # Convert email into TF-IDF features
            message_vector = vectorizer.transform([message])

            # Predict
            result = model.predict(message_vector)[0]

            # Convert prediction
            if result == 1 or str(result).lower() == "spam":
                prediction = "SPAM"
            else:
                prediction = "NOT SPAM"

            # Confidence
            if hasattr(model, "predict_proba"):

                probabilities = model.predict_proba(
                    message_vector
                )[0]

                confidence = round(
                    max(probabilities) * 100,
                    2
                )

            else:
                confidence = None

            # Save result
            save_prediction(
                message,
                prediction,
                confidence
            )

    history = get_history()

    return render_template(
        "index.html",
        prediction=prediction,
        confidence=confidence,
        message=message,
        history=history
    )


# -------------------------------------------------
# DASHBOARD DATA
# -------------------------------------------------

@app.route("/dashboard")
def dashboard():

    connection = sqlite3.connect(DATABASE)

    cursor = connection.cursor()

    # Total emails
    cursor.execute("""
        SELECT COUNT(*)
        FROM email_history
    """)

    total = cursor.fetchone()[0]

    # Spam count
    cursor.execute("""
        SELECT COUNT(*)
        FROM email_history
        WHERE prediction = 'SPAM'
    """)

    spam = cursor.fetchone()[0]

    # Not spam count
    cursor.execute("""
        SELECT COUNT(*)
        FROM email_history
        WHERE prediction = 'NOT SPAM'
    """)

    not_spam = cursor.fetchone()[0]

    # Average confidence
    cursor.execute("""
        SELECT AVG(confidence)
        FROM email_history
    """)

    average_confidence = cursor.fetchone()[0]

    if average_confidence:
        average_confidence = round(
            average_confidence,
            2
        )
    else:
        average_confidence = 0

    # Recent history
    connection.row_factory = sqlite3.Row

    cursor = connection.cursor()

    cursor.execute("""
        SELECT *
        FROM email_history
        ORDER BY id DESC
        LIMIT 20
    """)

    history = cursor.fetchall()

    connection.close()

    return render_template(
        "dashboard.html",
        total=total,
        spam=spam,
        not_spam=not_spam,
        average_confidence=average_confidence,
        history=history
    )


# -------------------------------------------------
# START APPLICATION
# -------------------------------------------------

if __name__ == "__main__":

    init_database()

    app.run(debug=True)