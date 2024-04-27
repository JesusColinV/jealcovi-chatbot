# app/vector_db/qdrant.py

from qdrant_client import QdrantClient
from .base_vector_db import BaseVectorDB

class QdrantVectorDB(BaseVectorDB):
    def __init__(self, host="localhost", port=6333, collection_name="my_collection"):
        super().__init__()
        self.client = QdrantClient(host=host, port=port)
        self.collection_name = collection_name

    def create_collection(self, vector_size, distance="Cosine"):
        self.client.recreate_collection(
            collection_name=self.collection_name,
            vectors_config=qdrant_client.models.VectorParams(size=vector_size, distance=distance),
        )

    def insert_vectors(self, vectors, ids):
        self.client.upsert(
            collection_name=self.collection_name,
            points=vectors,
            ids=ids
        )

    def search_vectors(self, query_vector, top_k):
        search_result = self.client.search(
            collection_name=self.collection_name,
            query_vector=query_vector,
            top=top_k
        )
        return search_result

    # ... Implement other methods as needed (e.g., update, delete)