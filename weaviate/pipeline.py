
import pandas as pd 
from google.cloud import storage
import io
import weaviate
import weaviate.classes as wvc
from summary import generate_summary, embed_summary
from init_collection import create_weaviate_collection_if_not_exists
from weaviate_client import wv_client
import logging 

logging.basicConfig(level=logging.INFO)

storage_client = storage.Client()
bucket = storage_client.bucket("strava_raw_data")
blob = bucket.blob(f"2025/09/26.json.gz")


data_bytes = blob.download_as_bytes()

df = pd.read_json(io.BytesIO(data_bytes),compression='gzip',lines=True)

df['summary']= df.apply(generate_summary,axis=1)
df['vector']= df['summary'].apply(embed_summary)

create_weaviate_collection_if_not_exists("strava_collection")
collection = wv_client.collections.use("strava_collection")


with collection.batch.dynamic() as batch:
    for _, row in df.iterrows():
        properties={
            "activity_id": row["id"],
            "name": row["name"],
            "start_date": row["start_date"],
            "summary": row['summary'],
        }
        batch.add_object(properties=properties, vector=row['vector'])

        if batch.number_errors > 10:
            logging.info("Batch import stopped due to excessive errors.")
            break

failed_objects = collection.batch.failed_objects
if failed_objects:
    logging.info(f"Number of failed imports: {len(failed_objects)}")

        
wv_client.close()