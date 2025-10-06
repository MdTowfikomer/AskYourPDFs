from vector_db import QdrantStorage

storage = QdrantStorage()

# Check collection exists
try:
    info = storage.client.get_collection("docs")
    print(f"✓ Collection exists")
    print(f"  Points count: {info.points_count}")
    print(f"  Vector dimension: {info.config.params.vectors.size}")
    
    if info.points_count == 0:
        print("\n⚠️  Collection is EMPTY! You need to ingest documents first.")
except Exception as e:
    print(f"✗ Error: {e}")