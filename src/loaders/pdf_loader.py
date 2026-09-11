from src.core.schemas import Document
from src.loaders.base import BaseLoader
from typing import List
from langchain_community.document_loaders import PyPDFLoader


class PDFLoader(BaseLoader):

    def load(self, file_path: str):
        print(f"Loading {file_path}")

        loader=PyPDFLoader(file_path)
        documents = loader.load()
        return documents