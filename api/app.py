from fastapi import FastAPI
from langchain_groq import ChatGroq
from langchain.prompts import ChatPromptTemplate
from langserve import add_routes
import uvicorn 
import os
from langchain_community.llms import Ollama
from dotenv import load_dotenv

load_dotenv()  # Just load the .env file

os.environ["GROQ_API_KEY"]= os.getenv("GROQ_API_KEY")

app = FastAPI(
    title = "Langchain Server",
    version = "0.1",
    description = "A Simple API Server"
)

add_routes(
    app,
    ChatGroq(),
    path="/groq"

)

model =ChatGroq()

llm =Ollama(model="llama2")

prompr1 = ChatPromptTemplate.from_template("Write me an essay about {topic} with 100 words")
prompr2 = ChatPromptTemplate.from_template("Write me an poem about {topic} with 100 words")

add_routes(
    app,
    prompr1 | model,
    path="/essay"
)

add_routes(
    app,
    prompr2 | model,
    path="/poem"
)

if __name__ == "__main__":
    uvicorn.run(app, host="localhost", port=8000)