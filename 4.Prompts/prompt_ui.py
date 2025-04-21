from langchain_openai import ChatOpenAI
from dotenv import load_dotenv
import streamlit as st
from langchain_core.prompts import PromptTemplate, load_prompt

# Load environment variables (your OpenAI API key, etc.)
load_dotenv()

# Initialize the model
model = ChatOpenAI(temperature=0.7)

template = load_prompt('template.json')
# Streamlit UI
st.header('Research Tool')

user_input = st.text_input('Enter your prompt')

if st.button('Summarize'):
    result = model.invoke(user_input)
    st.write(result.content)
