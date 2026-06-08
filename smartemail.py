import streamlit as st
import google.generativeai as genai
genai.configure(api_key="API KEY")
model=genai.GenerativeModel("gemini-2.5-flash")
st.title("Mail Maestro")
prompt=st.text_input("Enter your title")
a="you are an email generator, you will be given a topic you have to draft a email on that topic, include the tone adjustment.And give the email in the format of subject,body and signature"
if st.button("submit"):
    response=model.generate_content(a+prompt)
    st.write(response.text)