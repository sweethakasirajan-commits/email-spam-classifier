from flask import Flask, render_template, request
import joblib

app = Flask(__name__)

# Load trained model and TF-IDF vectorizer
model = joblib.load("model/spam_model.pkl")
vectorizer = joblib.load("model/tfidf_vectorizer.pkl")


@app.route("/", methods=["GET", "POST"])
def home():

    prediction = None
    email = ""

    if request.method == "POST":

        email = request.form["email"]

        # Convert email text into TF-IDF features
        email_tfidf = vectorizer.transform([email])

        # Predict spam or not spam
        result = model.predict(email_tfidf)[0]

        if result == 1:
            prediction = "SPAM EMAIL"
        else:
            prediction = "NOT SPAM"

    return render_template(
        "index.html",
        prediction=prediction,
        email=email
    )


if __name__ == "__main__":
    app.run(debug=True)