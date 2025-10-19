
import pandas as pd 
from google.cloud import storage
import io
from summary import generate_summary, embed_summary
import logging 

logging.basicConfig(level=logging.INFO)

storage_client = storage.Client()
bucket = storage_client.bucket("strava_raw_data")

blob = bucket.blob(f"2025/08/21.json.gz")


data_bytes = blob.download_as_bytes()

df = pd.read_json(io.BytesIO(data_bytes),compression='gzip',lines=True)
print(df)
df['summary']= df.apply(generate_summary,axis=1)
df['vector']= df['summary'].apply(embed_summary)

print(df[['summary','vector']])