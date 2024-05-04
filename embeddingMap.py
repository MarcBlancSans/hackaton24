import torch

class EmbeddingMap:
    def __init__(self):
        """Initializes an empty embedding map."""
        self.embeddings = {}

    def add_embedding(self, emb_id, embedding, index):
        """Adds an embedding with the specified ID and index.
        
        Args:
            emb_id (str): The ID of the embedding.
            embedding (list or torch.Tensor): The embedding vector.
            index (int): The index associated with the embedding.
        """
       
        self.embeddings[emb_id] = (embedding, index)

    def get_embedding(self, emb_id):
        """Retrieves an embedding by its ID.
        
        Args:
            emb_id (str): The ID of the embedding.
            
        Returns:
            tuple: A tuple containing the embedding vector and index associated with the ID.
        """
        return self.embeddings.get(emb_id)

    def remove_embedding(self, emb_id):
        """Removes an embedding by its ID.
        
        Args:
            emb_id (str): The ID of the embedding to remove.
        """
        if emb_id in self.embeddings:
            del self.embeddings[emb_id]
    
    def size(self):
        """Returns the number of embeddings stored in the map."""
        return len(self.embeddings)
