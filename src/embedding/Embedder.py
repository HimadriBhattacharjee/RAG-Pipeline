from sentence_transformers import SentenceTransformer
from langchain_core.embeddings import Embeddings
from config.settings import settings
from typing import List




class SentenceTransformer_Embedder(Embeddings):
    def __init__(self):
        self.model = SentenceTransformer(model=settings.EMBEDDING_MODEL)

    #Embed a list of documents using the SentenceTransformer model.
    def embed_documents(self, texts:list[str]) -> List[List[float]]:

        embeddings=self.model.encode(texts)
    
        return embeddings.tolist()

    def embed_query(self, text:str) -> List[float]:
        embedding=self.model.encode(text)
    
        return embedding.tolist()