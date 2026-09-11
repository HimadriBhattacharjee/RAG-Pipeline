from pydantic import BaseModel

class Document(BaseModel):
    content: str
    metadata: dict

class chunk(BaseModel):
    content: str
    metadata: dict
    chunk_index: int
class query(BaseModel):
    query_text: str
    top_k: int = 10
