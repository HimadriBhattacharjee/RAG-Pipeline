from pydantic_settings import BaseSettings,SettingsConfigDict
import os
from dotenv import load_dotenv
from pathlib import Path


load_dotenv()


class Settings(BaseSettings):
    PDF_PATH: Path = Path(os.getenv("PDF_PATH"))
    groq_API_KEY: str
    EMBEDDING_MODEL: str = "sentence-transformers/all-MiniLM-L6-v2"
    LLM_MODEL: str = "llama3.2"
    RETRIEVAL_TOP_K: int = 5
    CHUNK_SIZE:int =500
    CHUNK_OVERLAP:int =100
    model_config = SettingsConfigDict(env_file=".env")
    persist_directory:str =os.getenv("PERSIST_DIRECTORY")


settings=Settings()