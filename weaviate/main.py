import weaviate
import pandas as pd 
import weaviate.classes as wvc
from summary import generate_summary
from sentence_transformers import SentenceTransformer


client = weaviate.connect_to_local()

data = pd.read_json("/Users/thomashilger/Desktop/AskMyRun/weaviate/2025-10-3.json",lines=True)

print(data)

model = SentenceTransformer("BAAI/bge-m3")



objects = []
for index, row in data.iterrows():
    summary = generate_summary(row)
    print(f"Generated summary for row {index}")
    vector = model.encode(summary)



    objects.append(wvc.data.DataObject(
        properties={
            "activity_id": row["id"],
            "name": row["name"],
            "start_date": row["start_date"],
            "summary": summary,
        },
        vector=vector
    ))

questions = client.collections.use("strava_collection")
questions.data.insert_many(objects)

client.close()