from openai import OpenAI

class LLM:
    def __init__(self,base_url="http://localhost:11434/v1",api_key='ollama'):
        self.client=OpenAI(base_url=base_url,api_key=api_key)
    
    def generate_response(self,prompt:str,temperature:float=0.7):
        response=self.client.chat.completions.create(model='qwen-local',messages=[{"role":"system","content":'You answer only based on the context provided.'}
                                                                                ,{"role":"user","content":prompt}],temperature=temperature)
        return response.choices[0].message.content