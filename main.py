import streamlit as st
import numpy as np
import pandas as pd
import tensorflow as tf
import joblib
import json

# Load the trained model
@st.cache_resource
def load_model():
    model = tf.keras.models.load_model('autoencoder_model.keras')
    return model

# Load the scaler
@st.cache_resource
def load_scaler():
    scaler = joblib.load('scaler.joblib')
    return scaler

# Load the scaler parameters (optional)
@st.cache_resource
def load_scaler_params():
    with open("scaler_params.json", "r") as f:
        params = json.load(f)
    return params

# Calculate reconstruction error threshold (from saved training logic)
threshold = 0.5  # Replace with your threshold value

# App title and description
st.title("Credit Card Fraud Detection")
st.write("""
This web application allows users to upload transaction data to identify potential fraud using an autoencoder model.
""")

# Upload CSV file
uploaded_file = st.file_uploader("Upload your credit card transaction CSV file", type=["csv"])

if uploaded_file:
    # Read uploaded data
    data = pd.read_csv(uploaded_file)

    # Check for 'Class' column to avoid using true labels in predictions
    if 'Class' in data.columns:
        data = data.drop(columns=['Class'])

    st.write("Uploaded Data Preview:")
    st.dataframe(data.head())

    # Preprocess data
    scaler = load_scaler()
    scaled_data = scaler.transform(data)

    # Load model and predict
    model = load_model()
    reconstruction = model.predict(scaled_data)
    reconstruction_error = np.mean(np.power(scaled_data - reconstruction, 2), axis=1)

    # Classify transactions based on threshold
    predictions = [1 if err > threshold else 0 for err in reconstruction_error]

    # Add predictions to data
    results = data.copy()
    results['Fraud_Prediction'] = predictions
    results['Reconstruction_Error'] = reconstruction_error

    st.write("Results:")
    st.dataframe(results)

    # Download results
    csv = results.to_csv(index=False)
    st.download_button("Download Predictions as CSV", csv, "predictions.csv", "text/csv")

# Footer
st.write("---")
st.write("Developed with ❤️ using Streamlit")
