# Heart_Disease_App.py

import numpy as np
import pickle
import streamlit as st
from predictive_system import Heart_prediction

# Streamlit App
def main():
    st.title('Heart Disease Prediction Web App (13 Features)')

    # Input fields for 13 features
    age = st.text_input('1. Age')
    sex = st.text_input('2. Sex (1 = male, 0 = female)')
    cp = st.text_input('3. Chest Pain Type (0–3)')
    trestbps = st.text_input('4. Resting Blood Pressure')
    chol = st.text_input('5. Serum Cholesterol (mg/dl)')
    fbs = st.text_input('6. Fasting Blood Sugar > 120 mg/dl (1 = true, 0 = false)')
    restecg = st.text_input('7. Resting ECG Results (0–2)')
    thalach = st.text_input('8. Maximum Heart Rate Achieved')
    exang = st.text_input('9. Exercise Induced Angina (1 = yes, 0 = no)')
    oldpeak = st.text_input('10. ST Depression Induced by Exercise')
    slope = st.text_input('11. Slope of the Peak Exercise ST Segment (0–2)')
    ca = st.text_input('12. Major Vessels Colored by Fluoroscopy (0–3)')
    thal = st.text_input('13. Thalassemia (1 = normal, 2 = fixed defect, 3 = reversible defect)')

    diagnosis = ""

    if st.button('Heart Disease Test Result'):
        try:
            input_data = [
                float(age), float(sex), float(cp), float(trestbps), float(chol),
                float(fbs), float(restecg), float(thalach), float(exang),
                float(oldpeak), float(slope), float(ca), float(thal)
            ]
            diagnosis = Heart_prediction(input_data)
        except ValueError:
            diagnosis = "⚠️ Please enter valid numeric values for all fields."

    st.success(diagnosis)

if __name__ == '__main__':
    main()
