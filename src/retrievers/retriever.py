from langchain_core.documents import Document
from typing import List
from config.settings import settings


class Retriever:
    def __init__(self, vectordb:str):
        self.retriever = self.vectordb.get_retriever(settings.RETRIEVAL_TOP_K)
        

    def retrieve(self, query: str) -> list[Document]:
        documents=self.retriever.invoke(query)
        return documents
    