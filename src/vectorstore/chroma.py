from langchain_chroma import Chroma
from config.settings import settings



class vectordb:

    def __init__(self,persist_directory:str,embedding_function):
        self.persist_directory=persist_directory
        self.embedding_function=embedding_function
        self.db = Chroma(
                    collection_name="Langchain_Collection",
                    embedding_function=self.embedding_function,
                    persist_directory=self.persist_directory
                    )


    def create_chroma_vectordb(self):
        
        return self.db
    


