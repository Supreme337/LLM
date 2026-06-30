from sentence_transformers import SentenceTransformer
from config import Config

model_name=Config.embedding_model_name
embedding_model=SentenceTransformer(model_name)

class Retriever:
    def __init__(self,vector_store):
        self.collection=vector_store.collection

    def search(self,query,k=Config.top_k):
        query_embeddings=embedding_model.encode(query,normalize_embeddings=True)
        results=self.collection.query(
            query_embeddings=[query_embeddings.tolist()],
            n_results=k,include=['documents','metadatas','distances']
        )
    