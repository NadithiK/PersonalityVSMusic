# app.py

import streamlit as st
import joblib
import numpy as np

# Load model (make sure this file exists in the same directory)
model = joblib.load('music_model.pkl')

st.title("Music Recommendation Based on Personality")

# MBTI questions
st.header("Answer the following to determine your MBTI type:")

q1 = st.radio("When it comes to socialising:", ("Extraversion", "Introversion"))
q2 = st.radio("When processing information:", ("Sensing", "Intuition"))
q3 = st.radio("When making decisions:", ("Thinking", "Feeling"))
q4 = st.radio("When planning your day or tasks:", ("Judging", "Perceiving"))

# Build MBTI type
mbti = ""
mbti += "E" if q1 == "Extraversion" else "I"
mbti += "S" if q2 == "Sensing" else "N"
mbti += "T" if q3 == "Thinking" else "F"
mbti += "J" if q4 == "Judging" else "P"

st.markdown(f"**Your MBTI Type:** `{mbti}`")

if st.button("Predict"):
    try:
        # If your model expects encoded input, make sure to pre-process mbti accordingly
        prediction = model.predict([mbti])  # May need transformation to match training input
        st.success(f"🎵 Based on your personality type, we recommend: {prediction[0]}")
    except Exception as e:
        st.error(f"Prediction failed: {e}")
