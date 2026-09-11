from abc import ABC, abstractmethod
from typing import List
from src.core.schemas import Document

class BaseLoader(ABC):
    @abstractmethod
    def load(self, file_path: str) -> List[Document]:
        """Load and parse file into Documents."""
        pass