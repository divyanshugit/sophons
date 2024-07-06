# from qdrant_client import QdrantClient
from qdrant_client import QdrantClient, models
from dotenv import load_dotenv
import os

load_dotenv()

QDRANT_INDEX_URL = os.environ.get("QDRANT_INDEX_URL")
QDRANT_API_KEY = os.environ.get("QDRANT_API_KEY")
collection_names = ["complete_summary", "original_content"]

qdrant_client = QdrantClient(
    url=QDRANT_INDEX_URL,
    api_key=QDRANT_API_KEY,
)

for collection_name in collection_names:
    qdrant_client.create_collection(
        collection_name=f"{collection_name}",
        vectors_config=models.VectorParams(
            size=1024,
            distance=models.Distance.COSINE,
        ),
    )
