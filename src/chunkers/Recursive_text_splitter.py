from src.chunkers.base import BaseChunker
from src.core.schemas import Document, chunk
from langchain_text_splitters import RecursiveCharacterTextSplitter
from typing import List
from config.settings import Settings


class RecursiveChunker(BaseChunker):
    def __init__(self, settings: Settings):
        self.chunk_size = settings.CHUNK_SIZE
        self.chunk_overlap = settings.CHUNK_OVERLAP

    def chunk(self, documents: List[Document]) -> List["chunk"]:
        text_splitter = RecursiveCharacterTextSplitter(
            chunk_size=self.chunk_size,
            chunk_overlap=self.chunk_overlap,
            length_function=len,
        )
        chunks = text_splitter.split_text(documents.content)
        return [
            chunk(content=chunk, metadata=documents.metadata, chunk_index=i)
            for i, chunk in enumerate(chunks)
        ]
    
    