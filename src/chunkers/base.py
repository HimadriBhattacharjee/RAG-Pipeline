from abc import ABC, abstractmethod
from typing import List
from src.core.schemas import Document,chunk

class BaseChunker(ABC):
    @abstractmethod
    def chunk(self, document: Document) -> List[chunk]:
        """Split a document into chunks."""
        pass