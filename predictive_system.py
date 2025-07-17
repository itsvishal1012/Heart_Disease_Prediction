# predictive_system.py

import numpy as np
import pickle

# Load model and scaler
loaded_model = pickle.load(open('trained_model.sav', 'rb'))
scaler = pickle.load(open('scaler.sav', 'rb'))

# Prediction function
def Heart_prediction(input_data):
    input_array = np.asarray(input_data).reshape(1, -1)
    input_scaled = scaler.transform(input_array)
    prediction = loaded_model.predict(input_scaled)

    if prediction[0] == 1:
        return "✅ The person has heart disease."
    else:
        return "❌ The person does not have heart disease."

# Test example (13 features)
input_data = (63, 1, 3, 145, 233, 1, 0, 150, 0, 2.3, 0, 0, 1)

# Run prediction
result = Heart_prediction(input_data)
print(result)
