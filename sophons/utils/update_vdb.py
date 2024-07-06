from dotenv import load_dotenv
import os
import cohere
from qdrant_client import QdrantClient, models
from llama_index.vector_stores.qdrant import QdrantVectorStore
from llama_index.core import ServiceContext, VectorStoreIndex

from llama_index.llms.cohere import Cohere
from llama_index.embeddings.cohere import CohereEmbedding
from llama_index.core.schema import Document

from sophons.utils.logger import logger

load_dotenv()

QDRANT_INDEX_URL = os.environ.get("QDRANT_INDEX_URL")
QDRANT_API_KEY = os.environ.get("QDRANT_API_KEY")
COHERE_API_KEY = os.environ.get("COHERE_API_KEY")
qdrant_client = QdrantClient(
    url=QDRANT_INDEX_URL,
    api_key=QDRANT_API_KEY,
)


logger.info("Connecting to Qdrant VectoDB...")
vector_store = QdrantVectorStore(
    collection_name="original_content", client=qdrant_client
)

logger.info("Connecting to Cohere API...")
embed_model = CohereEmbedding(
    cohere_api_key=COHERE_API_KEY,
    model_name="embed-english-v3.0",
    input_type="search_query",
)

# Create the service context with the cohere model for generation and embedding model
logger.info("Creating service context...")
service_context = ServiceContext.from_defaults(
    llm=Cohere(api_key=COHERE_API_KEY, model="command"), embed_model=embed_model
)

logger.info("Creating index...")
index = VectorStoreIndex.from_vector_store(
    vector_store=vector_store, service_context=service_context
)

print("***" * 10)
print(vector_store.__dict__)
print("***" * 10)
print(embed_model.__dict__)
print("***" * 10)
print(service_context.__dict__)
print("***" * 10)
print(index.__dict__)
print("***" * 10)
# load text data
with open("/Users/divyanshu/dev/sophons/sophons/tmp_data/data.txt", "r") as f:
    data = f.readlines()

# convert data to string

data = "".join(data)

document = Document(
    text=data,
    metadata={
        "topic": "synthetic-data",
    },
)

logger.info("Inserting document into the index...")
index.insert(document)

logger.info("Creating payload index...")
qdrant_client.create_payload_index(
    collection_name="original_content",
    field_name="metadata.topic",
    field_type=models.PayloadSchemaType.KEYWORD,
)
logger.info("Updating collection...")
qdrant_client.update_collection(
    collection_name="original_content",
    hnsw_config=models.HnswConfigDiff(payload_m=16, m=0),
)
logger.info("Finished updating collection...")
