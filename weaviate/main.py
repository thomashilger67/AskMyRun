import weaviate
import pandas as pd 
import weaviate.classes as wvc
from weaviate_client import wv_client

collection = wv_client.collections.use("strava_collection")
response = collection.aggregate.over_all(total_count=True)

print(response.total_count)

wv_client.close()