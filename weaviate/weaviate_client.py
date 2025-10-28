import weaviate
import weaviate.classes as wvc
import os 
from dotenv import load_dotenv
load_dotenv()

wv_client = weaviate.connect_to_custom(
    http_host=os.getenv("WEAVIATE_HOST"),
    http_port=os.getenv("WEAVIATE_HTTP_PORT"),
    http_secure=False,
    grpc_host=os.getenv("WEAVIATE_HOST"),
    grpc_port=os.getenv("WEAVIATE_GRPC_PORT"),
    grpc_secure=False,
)