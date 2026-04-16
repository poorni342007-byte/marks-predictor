import streamlit as st
from sklearn.externals import joblib

# Load the trained model
model = joblib.load("model.pk")

st.title("Student Marks Prediction App")
st.write("Enter the number of study hours and get the predicted marks.")

# User input for hours
hours = st.number_input("Hours Studied", min_value=0.0, step=0.1)

# When the user clicks the predict button
if st.button("Predict Marks"):
    # Make prediction
    prediction = model.predict([[hours]])
    st.write(f"Predicted Marks: {prediction[0]:.2f}")
