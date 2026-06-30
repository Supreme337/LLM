import chromadb
from config import Config

class VectorStore:
    def __init__(self,collection_name:str):
        self.PersistentClient=chromadb.Client()
        self.collection=self.PersistentClient.get_or_create_collection(collection_name)
    
    def add_documents(self,documents,embeddings):
        ids=[doc["id"] for doc in documents]
        metadatas=[doc["metadata"] for doc in documents]
        self.collection.add(
            documents=[doc["text"] for doc in documents],
            embeddings=embeddings,metadatas=metadatas,ids=ids)
        
    def count(self):
        return self.collection.count()