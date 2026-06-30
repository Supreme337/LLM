from src.retriever import Retriever
from src.llm import LLM

class RAG:
    def __init__(self,vector_store):
        self.retriever=Retriever(vector_store)
        self.llm=LLM()
    
    def ask(self,question,k=5):
        results=self.retriever.search(question,k)
        context="\n\n".join(results['documents'][0])
        prompt=f"Answer the question based on the context below:\n\nContext: {context}\n\nQuestion: {question}\n\nAnswer:"
        answer=self.llm.generate_response(prompt)
        return {'question':question,
                'context':context,
                'answer':answer}