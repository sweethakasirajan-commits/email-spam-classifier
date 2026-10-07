# 📧 Email Spam Classification using Data Warehouse and Machine Learning

## 📌 Project Overview

Email Spam Classification is a machine learning-based project developed to identify whether an email message is Spam or Ham (Not Spam).

The project combines Data Warehouse concepts, text preprocessing, TF-IDF feature extraction, Machine Learning, SQLite database storage, and Flask to provide an end-to-end email classification system.

## 🎯 Objectives

- Classify email messages as Spam or Ham.
- Preprocess and clean email text data.
- Extract useful text features using TF-IDF.
- Train a machine learning classification model.
- Store prediction history in a structured database.
- Provide a web interface for email classification.
- Display prediction confidence and classification history.

## 🏗️ System Workflow

Email Dataset
      ↓
Data Cleaning & Preprocessing
      ↓
TF-IDF Feature Extraction
      ↓
Machine Learning Model
      ↓
Spam / Ham Prediction
      ↓
Database / Data Warehouse
      ↓
Flask Web Application
      ↓
Prediction Result & History

## 🗄️ Data Warehouse Component

The project uses a Data Warehouse approach to organize email classification information.

### Fact Table

fact_email_classification

| Field | Description |
|---|---|
| email_id | Unique email identifier |
| email_date | Date of email |
| subject | Email subject |
| message | Email content |
| actual_label | Actual Spam/Ham label |
| predicted_label | Model prediction |
| model_confidence | Prediction confidence |

The stored information can be used for analyzing spam patterns, prediction results, and model performance.

## 🤖 Machine Learning

The project uses:

- TF-IDF for converting text into numerical features.
- Multinomial Naive Bayes for email classification.
- Joblib for saving and loading the trained model and TF-IDF vectorizer.

## 📊 Model Performance

| Metric | Result |
|---|---:|
| Accuracy | 96.5% |
| Precision | 100% |
| Recall | 73.83% |
| F1-Score | 84.94% |

## 🚀 Application Versions

### 🟢 Basic Version

The main project contains a simple Flask web application for:

- Entering email content
- Predicting Spam or Not Spam
- Displaying the classification result

### 🔵 Advanced Version

The advanced_app folder contains an improved version with:

- Improved user interface
- Spam / Not Spam prediction
- Prediction confidence
- Prediction history
- SQLite database
- Dashboard
- Email statistics
- Recent prediction records

## 🛠️ Technologies Used

- Python
- Flask
- Scikit-learn
- TF-IDF
- Multinomial Naive Bayes
- Joblib
- SQLite
- HTML
- CSS
- Data Warehouse
- SQL

## 📁 Project Structure

email-spam-classifier/
│
├── app.py
├── requirements.txt
├── README.md
│
├── model/
│   ├── spam_model.pkl
│   └── tfidf_vectorizer.pkl
│
├── templates/
│   └── index.html
│
└── advanced_app/
    ├── app.py
    │
    ├── model/
    │   ├── spam_model.pkl
    │   └── tfidf_vectorizer.pkl
    │
    └── templates/
        ├── index.html
        └── dashboard.html

## ▶️ How to Run the Basic Version

### 1. Clone the Repository

git clone https://github.com/sweethakasirajan-commits/email-spam-classifier.git
cd email-spam-classifier

### 2. Install Required Packages

pip install -r requirements.txt

### 3. Run the Application

python app.py

### 4. Open the Application

Open:

http://127.0.0.1:5000

## ▶️ Advanced Version

Go to the advanced application folder:

cd advanced_app

Then run:

python app.py

The advanced application provides the improved interface, prediction confidence, history, database storage, and dashboard.

## 🌐 Applications

- Email spam detection
- Automated email classification
- Spam pattern analysis
- Machine learning-based email filtering
- Data Warehouse analysis

## 🚀 Future Enhancements

- Improve model performance with additional datasets.
- Add more machine learning algorithms.
- Add interactive Data Warehouse dashboards.
- Add user authentication.
- Deploy the application online.
- Add advanced email analytics.

## 👩‍💻 Author

Swetha Kasirajan

CSE Student | Aspiring UI/UX Designer

## ⭐ Project Highlights

This project demonstrates the integration of Data Warehouse, Machine Learning, Natural Language Processing, and Web Application Development to solve a real-world email spam classification problem.
