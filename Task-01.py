import streamlit as st
import joblib
import pandas as pd
import numpy as np

# Load the trained model
model = joblib.load("churn_model.pkl")

# Streamlit App UI
st.title("📊 Customer Churn Prediction App")
st.write("Predict whether a customer will churn based on their details.")

# User inputs
age = st.number_input("Age", min_value=18, max_value=100, value=30)
tenure = st.number_input("Tenure (Months)", min_value=0, max_value=100, value=12)
usage_frequency = st.number_input("Usage Frequency", min_value=0, max_value=30, value=5)
support_calls = st.number_input("Support Calls", min_value=0, max_value=20, value=1)
payment_delay = st.selectbox("Payment Delay?", ["No", "Yes"])
subscription_type = st.selectbox("Subscription Type", ["Basic", "Premium"])
contract_length = st.selectbox("Contract Length", ["Monthly", "Yearly"])

# Convert categorical inputs to numeric
payment_delay = 1 if payment_delay == "Yes" else 0
subscription_type = 1 if subscription_type == "Premium" else 0
contract_length = 1 if contract_length == "Yearly" else 0

# Create input DataFrame
input_data = pd.DataFrame([[age, tenure, usage_frequency, support_calls, payment_delay, subscription_type, contract_length]],
                          columns=["Age", "Tenure", "Usage Frequency", "Support Calls", "Payment Delay", "Subscription Type", "Contract Length"])

# Predict button
if st.button("Predict Churn"):
    prediction = model.predict(input_data)
    result = "Churn" if prediction[0] == 1 else "Not Churn"
    st.subheader(f"🛑 Prediction: {result}")
