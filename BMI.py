import streamlit as st
st.title("BMI Calculator")

with st.form("BMI calculator"):
    x1,x2,x3 = st.columns([3,2,1])
with x1:

    a1 = st.number_input("Enter Your Weight in Kgs")
with x2:

    a2 = st.number_input("Enter Your Height in Meters")
with x3:
        submit = st.form_submit_button("Calculate")

if submit:
    BMI = (a1 / (a2**2))
    if BMI < 18.5:
        st.error("Your Are Underweight")
    elif BMI >= 18.5 and BMI < 24.9:
        st.success("WOW ! Healthy")
    elif BMI > 25 and BMI <=29.9:
        st.warning("Your Over Weight")
    elif BMI >30:
        st.error("Obese")
