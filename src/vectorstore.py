import os
from pinecone import Pinecone, ServerlessSpec
from dotenv import load_dotenv

load_dotenv()

pinecone_client = Pinecone(api_key=os.getenv("PINECONE_API_KEY"))
pinecone_index = pinecone_client.Index(os.getenv("PINECONE_INDEX_NAME"))

def store_in_pinecone(chunks, embeddings):

    vectors_to_upsert = []
    for i, (chunk, embedding) in enumerate(zip(chunks, embeddings)):
        vector_data = {
            "id":f"chunk_{i}",
            "values":embedding,
            "metadata":{
                "text":chunk,
                "chunk_index":i
            }
        }
        vectors_to_upsert.append(vector_data)
    
    #Upsert vectors in batches
    batch_size=100
    for i in range(0, len(vectors_to_upsert), batch_size):
        batch = vectors_to_upsert[i:i+batch_size]
        pinecone_index.upsert(vectors=batch, namespace="")
    