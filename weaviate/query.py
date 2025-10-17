import weaviate
import weaviate.classes as wvc
from sentence_transformers import SentenceTransformer


client = weaviate.connect_to_local()

print("client ready:" + str(client.is_ready()))

model = SentenceTransformer("BAAI/bge-m3")

query = model.encode("Activity with the max heartrate in bpm. Knowing that my ma heart rate is 195 bpm.")



questions = client.collections.use("strava_collection")

response = questions.query.near_vector(
    near_vector=query,
    limit=2,
    return_metadata=wvc.query.MetadataQuery(certainty=True)
)

print(response)

for o in response.objects:
    print(o.properties)
    print(o.metadata.certainty)
client.close()
