from dataclasses import dataclass

@dataclass
class Config:
    embedding_model_name="BAAI/bge-small-en-v1.5"
    collection_name='music_sales'
    db_path='chroma_db'
    base_url="http://localhost:11434/v1"
    model='qwen-local'
    top_k=5
    temperature=0