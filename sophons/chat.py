from dotenv import load_dotenv
import os
import cohere
from qdrant_client import QdrantClient, models
from llama_index.vector_stores.qdrant import QdrantVectorStore
from llama_index.core import ServiceContext, VectorStoreIndex

from llama_index.llms.cohere import Cohere
from llama_index.embeddings.cohere import CohereEmbedding
from llama_index.core.schema import Document
from llama_index.core.vector_stores.types import MetadataFilters, ExactMatchFilter
from llama_index.core.retrievers import VectorIndexRetriever

# from llama_index.retrievers import VectorIndexRetriever
from llama_index.core.response_synthesizers import get_response_synthesizer
from llama_index.core.query_engine import RetrieverQueryEngine
from llama_index.core.postprocessor import SimilarityPostprocessor
from llama_index.core.tools import FunctionTool

from sophons.utils.logger import logger


load_dotenv()

QDRANT_INDEX_URL = os.environ.get("QDRANT_INDEX_URL")
QDRANT_API_KEY = os.environ.get("QDRANT_API_KEY")
COHERE_API_KEY = os.environ.get("COHERE_API_KEY")


def chat(query: str, topic: str):

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

    logger.info("Creating service context...")
    service_context = ServiceContext.from_defaults(
        llm=Cohere(api_key=COHERE_API_KEY, model="command"), embed_model=embed_model
    )

    logger.info("Creating index...")
    index = VectorStoreIndex.from_vector_store(
        vector_store=vector_store, service_context=service_context
    )

    retriever = VectorIndexRetriever(index=index, similarity_top_k=5)

    synth = get_response_synthesizer(response_mode="refine")

    # construct query engine
    query_engine = RetrieverQueryEngine(
        retriever=retriever,
        response_synthesizer=synth,
        node_postprocessors=[SimilarityPostprocessor(similarity_cutoff=0.55)],
    )

    response = query_engine.query(query)
    return response


if __name__ == "__main__":
    response = chat("What is synthetic data?", "Synthetic Data")
    print(response)
