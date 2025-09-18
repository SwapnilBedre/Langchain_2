from langchain_groq import ChatGroq
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser

import streamlit as st
import os
from dotenv import load_dotenv

load_dotenv()  # Just load the .env file

os.environ["GROQ_API_KEY"]= os.getenv("GROQ_API_KEY")
# Langsmith Tracing
os.environ["LANGCHAIN_TRACING_V2"] = "true"
os.environ["LANGCHAIN_API_KEY"] = os.getenv("LANGCHAIN_API_KEY")

# Prompt Template

prompt = ChatPromptTemplate.from_messages(
    [
        ("system", "You are a helpful assistant. Please responce to the user query"),
        ("user", "question: {question}")
    ]
)

# Streamlit Framework

st.title("Langchain Demo with Groq")
input_text = st.text_input("search the topic you want")

# Groq LLM

llm = ChatGroq(model="llama-3.1-8b-instant")  # for small data,

output_parser = StrOutputParser()
chain = prompt | llm | output_parser

if input_text:
    st.write(chain.invoke({"question": input_text}))