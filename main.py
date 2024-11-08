import os
import streamlit as st
import google.generativeai as genai
from dotenv import load_dotenv
load_dotenv()


genai.configure(api_key=os.environ["GOOGLE_API_KEY"])

model = genai.GenerativeModel("gemini-1.5-pro-latest")

def get_response(question):
    response = model.generate_content(question)
    return response.text

st.set_page_config(page_title="CHATBOT")

st.title("ARTICLE GENERATOR CHATBOT")
input = st.text_input("Ask your query here: ",key='input')
submit = st.button("GENERATE")

if submit:
    response = get_response(input)
    st.subheader("Generated content is: ")
    st.write("Answer: ",response)

