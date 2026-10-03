import streamlit as st
st.title("Korean Learning App")
st.write("Annyeonghaseyo - Hello in Korean")
st.write("Gamsahamnida - Thank you")
st.write("Saranghae - I love you")
name = st.text_input("What is your name?")
if name:
    st.success(f"Bangapseumnida {name}")
