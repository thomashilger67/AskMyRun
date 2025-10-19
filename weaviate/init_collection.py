import weaviate
import weaviate.classes as wvc



def create_weaviate_collection(collection_name:str):
    """
    Create a Weaviate collection with a self provided vector.

    Parameters:
    - collection_name (str): The name of the collection.

    Returns:
    - None
    """
    
    client = weaviate.connect_to_local()

    logging.info("client ready:" + str(client.is_ready()))

    try :
        client.collections.create(
            "strava_collection",
            vector_config=wvc.config.Configure.Vectors.self_provided(),
        )
        logging.info(f"Weaviate collection '{collection_name}' created successfully.")
        client.close()
    except e: 
        logging.error(f"Error creating Weaviate collection '{collection_name}': {e}")



