import os
import streamlit as st
import google.generativeai as genai
from dotenv import load_dotenv
load_dotenv()

#os.environ["GOOGLE_API_KEY"] = "AIzaSyAjciWYj1Ag58ioKe5LJ-8BdGZ0dulJ284"
genai.configure(api_key=os.environ["GOOGLE_API_KEY"])

model = genai.GenerativeModel("gemini-pro")

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