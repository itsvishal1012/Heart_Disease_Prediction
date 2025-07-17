## ❤️ Heart Disease Prediction Web App
A machine learning-based web application built with Streamlit to predict the likelihood of heart disease using 13 clinical input features.

# 🧠 Overview
This project helps in predicting whether a person is likely to have heart disease based on key health indicators such as cholesterol levels, blood pressure, ECG results, and more. The app uses a pre-trained machine learning model to make predictions in real time.

# 🔍 Demo Screenshot

# 🚀 Features
📋 User-friendly interface to enter 13 health-related values.

🔐 Input validation with error messages for incorrect fields.

🧠 Pre-trained ML model for real-time heart disease predictions.

📉 Scales input values before prediction using a standard scaler.

✅ Clear result display: shows whether the person has heart disease or not.

# 🏗️ Project Structure

1.) heart.csv - Dataset used for training (uploaded)
2.) trained_model.sav - Serialized machine learning model
3.) scaler.sav - Serialized scaler object (StandardScaler)
4.) Heart_Disease_App.py - Streamlit front-end app script
5.) predictive_system.py - Backend prediction logic
6.) Screenshot.png - Interface screenshot
7.) Heart_prediction.ipynb - Notebook for training/experimentation
8.) README.md - You're here!

# 📥 Input Features (13 Total)
Feature	Description
1. Age	Age of the person
2. Sex	1 = male, 0 = female
3. Chest Pain Type (cp)	0–3 (Typical angina to asymptomatic)
4. Resting Blood Pressure	In mm Hg
5. Serum Cholesterol (chol)	In mg/dl
6. Fasting Blood Sugar (fbs)	>120 mg/dl → 1 (true), otherwise 0 (false)
7. Resting ECG (restecg)	0 = normal, 1 = ST-T abnormality, 2 = left ventricular hypertrophy
8. Max Heart Rate Achieved	In bpm
9. Exercise-Induced Angina (exang)	1 = yes, 0 = no
10. ST Depression (oldpeak)	Depression induced by exercise relative to rest
11. Slope of Peak ST Segment	0 = upsloping, 1 = flat, 2 = downsloping
12. Major Vessels (ca)	Number of major vessels (0–3) colored by fluoroscopy
13. Thalassemia (thal)	1 = normal, 2 = fixed defect, 3 = reversible defect

# 🧪 How It Works
User enters input into the Streamlit UI.

Inputs are converted to float and validated.

Inputs are scaled using a saved StandardScaler.

The model predicts the presence or absence of heart disease.

The result is displayed as either ✅ or ❌.

# 🖥️ Running the App
⚙️ Prerequisites
Python 3.8+

# 📦 Install Dependencies

pip install -r requirements.txt
If requirements.txt is not available, install manually:

pip install streamlit numpy scikit-learn

# ▶️ Run Streamlit App

streamlit run Heart_Disease_App.py

# 📁 Model & Scaler Notes
trained_model.sav: Contains the pre-trained classification model.

scaler.sav: Contains the scaler (used for feature normalization).

These must be present in the same directory as predictive_system.py.

# ⚠️ Common Issues
"Please enter valid numerical values for all fields": Ensure all inputs are filled with numbers.

Model not found error: Make sure trained_model.sav and scaler.sav exist and are properly saved.

# 📊 Model Accuracy
Accuracy and metrics like Precision, Recall, F1-Score can be found in the Heart_prediction.ipynb notebook, used during training.

## 👨‍💻 Author
Vishal Singh
Data Scientist & ML Enthusiast
