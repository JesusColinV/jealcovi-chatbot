# app/vector_db/base_vector_db.py

from abc import ABC, abstractmethod

class BaseVectorDB(ABC):
    """
    Abstract base class for vector databases, defining a common interface.
    """

    @abstractmethod
    def create_collection(self, vector_size, distance):
        """
        Creates a new collection with the specified vector size and distance metric.
        """
        pass

    @abstractmethod
    def insert_vectors(self, vectors, ids):
        """
        Inserts vectors with their corresponding IDs into the collection.
        """
        pass

    @abstractmethod
    def search_vectors(self, query_vector, top_k):
        """
        Searches for the top_k most similar vectors to the query_vector.
        """
        pass

    # ... Add more abstract methods for other functionalities as needed (e.g., update, delete)