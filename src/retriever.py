from sentence_transformers import SentenceTransformer
model_name= "BAAI/bge-small-en-v1.5"
embedding_model=SentenceTransformer(model_name)

class Retriever:
    def __init__(self,vector_store):
        self.collection=vector_store.collection

    def search(self,query,k=5):
        query_embeddings=embedding_model.encode(query,normalize_embeddings=True)
        results=self.collection.query(
            query_embeddings=[query_embeddings.tolist()],
            n_results=k
        )
        return results
