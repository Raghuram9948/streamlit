import streamlit as st
from datetime import datetime

st.title('HACKING YOUR PHONE')

if st.button(" Say hello" ):
    st.write("hello")

if st.checkbox("I Agree Terms and Conditons:"):
    st.write("THANK YOU")



st.subheader("1.Name input")
Name = st.text_input("Enter your Name : " , value = "RAGHURAM")
st.write(Name)

st.subheader("Radio Button")
st.radio( "Gender : " , options = ("Men", "Adult" , "Child"))

st.subheader(" 2.PHONE Password: ")
st.text_input(" Enter Your Password : " , type = "password" , help = " MADDAKUDU")


#today = datetime.today()
#date = st.date_input("DOb" , value = "today" , min_value = today , max_value = today.replace(today.year + 1))
#st.write(date)

st.subheader("Give permission :" )
x = st.selectbox(" Select Your options : " , options = ("messages","calls" , " photos"))
st.write("thanks  for your permission in :",x)

st.subheader("App Permissions- select any 2 Application : ")
st.multiselect(" Select Application : " , options = ( "What's App", "Instagram" ,"messages", "File Manager"))


st.button(" Submit Response")
