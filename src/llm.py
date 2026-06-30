from openai import OpenAI
from config import Config

class LLM:
    def __init__(self,base_url=Config.base_url,api_key='ollama'):
        self.client=OpenAI(base_url=base_url,api_key=api_key)
    
    def generate_response(self,prompt:str,temperature=Config.temperature):
        response=self.client.chat.completions.create(model=Config.model,messages=[{"role":"system","content":'You answer only based on the context provided.'}
                                                                                ,{"role":"user","content":prompt}],temperature=temperature)
        return response.choices[0].message.content