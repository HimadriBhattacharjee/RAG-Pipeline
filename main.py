from src.pipeline import pipeline
from fastapi import FastAPI
from pydantic import BaseModel



# Create FastAPI application
app = FastAPI(
    title="RAG API",
    description="FastAPI wrapper for the RAG application",
    version="1.0.0"
)

class Question(BaseModel):
    text: str

@app.post("/ask")
async def ask_question(question: Question):
    # Initialize the pipeline
    rag = pipeline()

    # Ingest documents and create the vector database
    rag.ingest()

    # Example question to ask
    question = "What is the main topic of the document?"

    # Ask the question and get the answer
    answer = rag.ask_question(question)

    print(f"Question: {question}")
    print(f"Answer: {answer}")