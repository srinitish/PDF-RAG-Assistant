import chromadb
import uuid
from embeddings import EmbeddingModel

class VectorStore:

    def __init__(self, collection_name="pdf_documents", persist_directory="data/vector_store"):

        self.collection_name = collection_name
        self.persist_directory = persist_directory

        self.client = chromadb.PersistentClient(path=self.persist_directory)

        self.collection = self.client.get_or_create_collection(
            name=self.collection_name
        )

        self.embedding_model = EmbeddingModel()


    def add_documents(self, chunks):

        texts = [chunk.page_content for chunk in chunks]

        embeddings = self.embedding_model.embed(texts)

        ids = [str(uuid.uuid4()) for _ in texts]

        self.collection.add(
            documents=texts,
            embeddings=embeddings,
            ids=ids
        )


    def search(self, query, k=3):

        query_embedding = self.embedding_model.embed([query])[0]

        results = self.collection.query(
            query_embeddings=[query_embedding],
            n_results=k
        )

        return results["documents"][0]