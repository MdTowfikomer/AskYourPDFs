from data_loader import embed_texts
from vector_db import QdrantStorage

# Test search directly
question = "What is machine learning?"
query_vec = embed_texts(question, input_type="search_query")

print(f"Query vector dimension: {len(query_vec)}")

storage = QdrantStorage()
try:
    results = storage.search(query_vec, top_k=5)
    print(f"Search successful!")
    print(f"Found {len(results['contexts'])} contexts")
    print(f"Sources: {results['sources']}")
except Exception as e:
    print(f"Search failed: {e}")
    import traceback
    traceback.print_exc()