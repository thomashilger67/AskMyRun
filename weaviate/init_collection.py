import weaviate
import weaviate.classes as wvc


client = weaviate.connect_to_local()

print("client ready:" + str(client.is_ready()))

client.collections.create(
    "strava_collection",
    vector_config=wvc.config.Configure.Vectors.self_provided(),
)

client.close()