# 📧 Email Spam Classification using Data Warehouse and Machine Learning

## 📌 Project Overview

Email Spam Classification is a machine learning-based project developed to identify whether an email message is **Spam** or **Ham (Not Spam)**.

The project combines **Data Warehouse concepts, text preprocessing, TF-IDF feature extraction, Machine Learning, and Flask** to provide an end-to-end email classification system.

## 🎯 Objectives

- Classify email messages as Spam or Ham.
- Preprocess and clean email text data.
- Extract useful text features using TF-IDF.
- Train a machine learning classification model.
- Store classification information in a structured Data Warehouse.
- Provide a simple web interface for users to test email messages.

## 🏗️ System Workflow

```text
Email Dataset
      ↓
Data Cleaning & Preprocessing
      ↓
TF-IDF Feature Extraction
      ↓
Machine Learning Model
      ↓
Spam / Ham Prediction

## 🗄️ Data Warehouse Component

The project uses a Data Warehouse approach to organize email classification information.

### Fact Table

**fact_email_classification**

| Field | Description |
|---|---|
| email_id | Unique email identifier |
| email_date | Date of email |
| subject | Email subject |
| message | Email content |
| actual_label | Actual Spam/Ham label |
| predicted_label | Model prediction |
| model_confidence | Prediction confidence |

The warehouse can be used for analyzing spam patterns, prediction results, and model performance.

## 🤖 Machine Learning

The project uses:

- **TF-IDF** for converting text into numerical features.
- **Multinomial Naive Bayes** for classifying email messages.
- **Joblib** for saving and loading the trained model and TF-IDF vectorizer.

## 📊 Model Performance

| Metric | Result |
|---|---:|
| Accuracy | 96.5% |
| Precision | 100% |
| Recall | 73.83% |
| F1-Score | 84.94% |

## 🛠️ Technologies Used

- Python
- Flask
- Scikit-learn
- TF-IDF
- Multinomial Naive Bayes
- Joblib
- HTML/CSS
- Data Warehouse
- SQL

## 📁 Project Structure

```text
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
└── templates/
    └── index.html

      ↓
Data Warehouse
      ↓
Flask Web Application
      ↓
Prediction Result
