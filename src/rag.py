from src.retriever import Retriever
from src.llm import LLM
from src.prompt_builder import PromptBuilder

class RAG:
    def __init__(self,vector_store):
        self.retriever=Retriever(vector_store)
        self.llm=LLM()
    
    def ask(self,question,k=5):
        results=self.retriever.search(question,k)
        context="\n\n".join(results['documents'][0])
        prompt=PromptBuilder.build(context,question)
        answer=self.llm.generate_response(prompt)
        return {'question':question,
                'context':context,
                'answer':answer,
                'sources':results['metadatas'][0]}