import weaviate
import pandas as pd 
import weaviate.classes as wvc

client = weaviate.connect_to_custom(
    http_host="34.155.19.255",
    http_port=8080,
    http_secure=False,
    grpc_host="34.155.19.255",
    grpc_port=50051,
    grpc_secure=False,
)

collection = client.collections.use("strava_collection")
response = collection.aggregate.over_all(total_count=True)

print(response.total_count)

client.close()