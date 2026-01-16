from langchain_community.vectorstores import Chroma
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_huggingface import HuggingFaceEmbeddings

class VectorStore:
    def __init__(self):
        self.embedder = HuggingFaceEmbeddings(model_name="all-MiniLM-L6-v2")
        self.db = Chroma(persist_directory="./chroma", embedding_function=self.embedder)

    def add_documents(self, docs):
        splitter = RecursiveCharacterTextSplitter(chunk_size=500, chunk_overlap=50)
        chunks = splitter.split_documents(docs)
        self.db.add_documents(chunks)
        self.db.persist()

    def search(self, query, k=4):
        return self.db.similarity_search(query, k=k)


class VectorStore:
    def __init__(self):
        self.embedder = HuggingFaceEmbeddings(model_name="all-MiniLM-L6-v2")
        self.db = Chroma(persist_directory="./chroma", embedding_function=self.embedder)

    def add_documents(self, docs):
        splitter = RecursiveCharacterTextSplitter(chunk_size=500, chunk_overlap=50)
        chunks = splitter.split_documents(docs)
        self.db.add_documents(chunks)
        self.db.persist()

    def search(self, query, k=4):
        return self.db.similarity_search(query, k=k)
