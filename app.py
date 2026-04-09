import streamlit as st

st.title("BMI Calculator")

weight = st.number_input("Weight (kg)", min_value=1.0, max_value=300.0, value=70.0, step=0.1)
height = st.number_input("Height (m)", min_value=0.5, max_value=2.5, value=1.75, step=0.01)

if st.button("Calculate BMI"):
    bmi = weight / (height * height)
    st.metric("Your BMI", f"{bmi:.2f}")
