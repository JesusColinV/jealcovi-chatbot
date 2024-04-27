from .base_vector_db import BaseVectorDB

def get_vector_db(db_type, **kwargs):
    """
    Factory function to get a vector database instance based on the provided type.
    """
    if db_type == "qdrant":
        from .qdrant import QdrantVectorDB
        return QdrantVectorDB(**kwargs)
    # Add more elif conditions for other vector database types
    else:
        raise ValueError(f"Unsupported vector database type: {db_type}")