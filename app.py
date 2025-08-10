import streamlit as st
import joblib
import pandas as pd

# Load pipeline
pipeline = joblib.load("model/pipeline.pkl")

st.title("Introvert vs Extrovert Predictor")

st.write("Answer the following questions to find out if you are more of an introvert or extrovert.")

time_spent_alone = st.slider("How many hours do you usually spend alone each day?", 0, 11)
stage_fear = st.radio("Do you experience stage fright or fear when speaking in front of others?", ["Yes", "No"])
social_event_attendance = st.slider("How often do you attend social events each month?", 0, 10)
going_outside = st.slider("How many days per week do you usually go outside your home?", 0, 7)
drained_after_socializing = st.radio("Do you feel drained or exhausted after socializing with people?", ["Yes", "No"])
friends_circle_size = st.slider("How many close friends do you have in your circle?", 0, 15)
post_frequency = st.slider("How often do you post on social media each week?", 0, 10)


if st.button("Predict"):
    input_data = pd.DataFrame([{
        "Time_spent_Alone": time_spent_alone,
        "Stage_fear": 1 if stage_fear == "Yes" else 0,
        "Social_event_attendance": social_event_attendance,
        "Going_outside": going_outside,
        "Drained_after_socializing": 1 if drained_after_socializing == "Yes" else 0,
        "Friends_circle_size": friends_circle_size,
        "Post_frequency": post_frequency,
    }])

    result = pipeline.predict(input_data)[0]
    label = "Extrovert" if result == 0 else "Introvert"
    st.success(f"You are most likely an **{label}**!")
