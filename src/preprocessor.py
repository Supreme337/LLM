import pandas as pd
from sentence_transformers import SentenceTransformer
from config import Config

def document_generator(df:pd.DataFrame):
    documents=[]
    for idx,row in df.iterrows():
        text=""
        for column in df.columns:
            text+=f"{column}:{row[column]}\n"
        documents.append(
            {
                "id": str(idx),
                "text": text,
                "metadata": {
                    "row": idx}})
    return documents

model_name=Config.embedding_model_name
embedding_model=SentenceTransformer(model_name)

def create_embeddings(documents):
    texts=[doc["text"] for doc in documents]
    embeddings=embedding_model.encode(texts,show_progress_bar=True,normalize_embeddings=True)
    return embeddings