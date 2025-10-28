import weaviate
import weaviate.classes as wvc
from weaviate_client import wv_client
import logging


def create_weaviate_collection_if_not_exists(collection_name:str):
    """
    Create a Weaviate collection with a self provided vector.

    Parameters:
    - collection_name (str): The name of the collection.

    Returns:
    - None
    """
    
    logging.info("client ready:" + str(wv_client.is_ready()))

    try :
        if wv_client.collections.exists(collection_name):
            logging.info(f"Weaviate collection '{collection_name}' already exists.")
        else: 
            wv_client.collections.create(
                collection_name,
                vector_config=wvc.config.Configure.Vectors.self_provided(),
            )
            logging.info(f"Weaviate collection '{collection_name}' created successfully.")
    except e: 
        logging.error(f"Error creating Weaviate collection '{collection_name}': {e}")
        wv_client.close()




