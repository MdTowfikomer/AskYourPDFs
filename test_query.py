from data_loader import embed_texts
from vector_db import QdrantStorage

# Test your query embedding
question = "What is machine learning?"
query_vec = embed_texts(question, input_type="search_query")

print(f"Query vector type: {type(query_vec)}")
print(f"Query vector length: {len(query_vec)}")

# Check collection
storage = QdrantStorage()
info = storage.client.get_collection("docs")
print(f"Collection dimension: {info.config.params.vectors.size}")

# Check if they match
if len(query_vec) == info.config.params.vectors.size:
    print("Dimensions match!")
else:
    print(f"MISMATCH: Query={len(query_vec)}, Collection={info.config.params.vectors.size}")