from openai import OpenAI
from dotenv import load_dotenv
import os
from typing import List, Dict

#loading the env variables package
load_dotenv()

#setup the Open AI key and embedding model
open_ai_key = OpenAI(api_key=os.getenv("OPEN_AI_KEY"))
embedding_model = "text-embedding-3-small"  # 1536 Dimension vectors


def create_embeddings(chunks: List[str]) -> List[List[float]]:
    embeddings = []
    for chunk in chunks:
        response = open_ai_key.embeddings.create(input=chunk, model=embedding_model)
        embeddings.append(response.data[0].embedding)
    print(embeddings)
    return embeddings
