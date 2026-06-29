from openai import OpenAI

class LLM:
    def __init__(self,base_url="http://localhost:127.0.0.1/v1",model="qwen-local",api_key='ollama'):
        self.client=OpenAI(base_url=base_url,model=model,api_key=api_key)
        self.model=model
    
    def generate_response(self,prompt:str,temperature:float=0.7):
        response=self.client.chat.completions.create(model=self.model,messages=[{"role":"system","content":'You answer only based on the context provided.'}
                                                                                ,{"role":"user","content":prompt}],temperature=temperature)
        return response.choices[0].message.content