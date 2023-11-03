# Q&A Chatbot

from langchain.llms import OpenAI
from dotenv import load_dotenv
import streamlit as st


# loading the env
load_dotenv()

def get_openai_response(message: str):
    llm = OpenAI(model_name="text-davinci-003", temperature=0.6)
    response= llm(message)
    return response

# UI 
st.set_page_config(page_title="Receipe Chat")
st.header('Receipe Chat')

input = st.text_input("Input: ", key="input")
res = get_openai_response(input)

generate_btn = st.button("Hungry!! Ask any receipe...")

if generate_btn:
    st.subheader("The response is")
    st.write(res)