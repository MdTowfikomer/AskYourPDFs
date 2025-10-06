from qdrant_client import QdrantClient
from qdrant_client.models import  VectorParams, Distance, PointStruct


class QdrantStorage:
    def __init__(self, url="http://localhost:6333", collection="docs", dim=1024):
        self.client = QdrantClient(url=url, timeout=30) # create Qdrant client
        self.collection = collection    #Stores collection names
        if not self.client.collection_exists(self.collection):  # check if collection exist
            self.client.create_collection(      # creates new collection
                collection_name=self.collection,
                # configuration for vectors
                # each vector will have 3072 numbers
                # use cosine similarity to compare vectors
                vectors_config=VectorParams(size=dim, distance=Distance.COSINE),
                # Distance.COSINE
                # Measures angle between vectors (good for text similarity)
                # Range -1(opposite) to 1(identical)
            )


    def upsert(self, ids, vectors, payloads):
        points = [PointStruct(id=ids[i], vector=vectors[i], payload=payloads[i]) for i in range(len(ids))]
        self.client.upsert(self.collection, points=points) # saves all points to the "docs" collection
        
    def search(self, query_vector, top_k: int = 5):
            result = self.client.search(
                collection_name=self.collection,    # Search in "docs" collection
                query_vector=query_vector,          # User's question as vector
                with_payload=True,                  # Include metadata (text,page, etc.)
                limit=top_k                         # Return top 5 results
            )       
            contexts = []
            sources = set()
            
            for r in result:
                payload = getattr(r, "payload", None) or {}
                # payload = r.payload if r.payload else {}
                text = payload.get("text", "")
                source = payload.get("source", "")
                if text:
                    contexts.append(text)
                    sources.add(source)

            return {"contexts": contexts, "sources": list(sources)}