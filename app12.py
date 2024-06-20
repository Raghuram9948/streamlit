import streamlit as st
from datetime import datetime

st.title("KORLAPATI")

st.subheader("1.Name input")
Name = st.text_input("Enter your Name : " , value = "RAGHURAM")
st.write(Name)

st.subheader(" 2. Password Input")
st.text_input(" Enter Your Password : " , type = "password" , help = " MADDAKUDU")

st.subheader("3 .Text Area")
st.text_area( "Describe  yourself" , height = 200 ,help = " who are you")
today = datetime.today()
date = st.date_input("DOb" , value = "today" , min_value = today , max_value = today.replace(today.year + 1))
st.write(date)
