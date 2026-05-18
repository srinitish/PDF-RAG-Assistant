from embeddings import EmbeddingModel

class Retriever:
    def __init__(self,collection):
        self.collection = collection
        self.embedding_model = EmbeddingModel()

    def retrieve(self,query):
        query_embedding = self.embedding_model.embed([query])

        results = self.collection.query(
            query_embeddings = query_embedding,
            n_results = 3
        )

        return results['documents'][0]
    