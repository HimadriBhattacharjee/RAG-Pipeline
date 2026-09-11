##It will connect all the modules together and run the pipeline
from config.settings import settings
from src.loaders.pdf_loader import PDFLoader
from src.chunkers.Recursive_text_splitter import RecursiveChunker
from src.embedding.Embedder import SentenceTransformer_Embedder
from src.vectorstore.chroma import vectordb
from src.retrievers.retriever import Retriever
from src.generation.llm import LLM_Generator



class pipeline:
    def __init__(self):
        self.settings = settings()
        self.loader = PDFLoader(settings.PDF_PATH)
        self.chunker = RecursiveChunker(settings.CHUNK_SIZE, settings.CHUNK_OVERLAP)
        self.embedding = SentenceTransformer_Embedder()
        self.vectorstore = vectordb(settings.persist_directory,self.embedding)
        self.retriver=None
        self.llm=LLM_Generator(settings.LLM_MODEL)



    def ingest(self):

        # PDF loading
        documents = self.loader.load()

        # Split into chunks
        chunks = self.chunker.chunk(documents)
        print(f"Created {len(chunks)} chunks from the documents.")

        # Store chunks(as well as their coresponding vector embeddings through embedding function) in the vector database
        self.db=self.vectorstore.create_chroma_vectordb()
        self.db.add_documents(chunks)

        # Create retriever
        self.retriver = Retriever(self.db,settings.RETRIEVAL_TOP_K)

    def ask_question(self,question:str)->str:
        # Retrieve relevant chunks
        retrieved_chunks = self.retriver.retrieve(question)

        # Combining retrieved chunks into a single string for LLM input
        context = " ".join(doc.page_content for doc in retrieved_chunks)

        # Create a prompt for the LLM
        prompt =  f"""
        You are a helpful RAG assistant.

        Answer the question using ONLY
        the provided context.

        If the answer is not present in the
        context, say:
        "I don't know based on the provided document."

        Context:
        {context}

        Question:
        {question}

        Answer:
        """

        # Generate answer using LLM
        answer = self.llm.generate_answer(prompt)
        return answer
    






            
        