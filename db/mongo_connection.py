from pymongo import MongoClient
from threading import Lock
from constants import DEFAULT_DB


class MongoDBConnector:
    """MongoDB class to create an instance."""
    _MONGO_URI = "mongodb://localhost:27017"
    _instance = None
    _lock = Lock()

    def __new__(cls, *args, **kwargs):
        if not cls._instance:
            with cls._lock:
                if not cls._instance:
                    cls._instance = MongoClient(cls._MONGO_URI)
        return cls._instance

    def __init__(self, *args, **kwargs):
        """MongoDB Initialiser."""
        print("*****Initialising MongoDB Instance.")


class MongoDB:
    """MongoDB."""
    _default_db = DEFAULT_DB
    _connector = MongoDBConnector()

    @classmethod
    def _get_collection(cls, **kwargs) -> any:
        collection_name = kwargs.get("collection_name")
        collection_obj = cls._connector.get_database(cls._default_db).get_collection(collection_name)
        return collection_obj


async def run_db_query(**kwargs) -> any:
    """Run db query."""
    collection_name = kwargs.get("collection_name")
    query_type = kwargs.get("query_type")
    query = kwargs.get("query")
    data = None
    if query_type == "find_one":
        data = MongoDB._get_collection(collection_name=collection_name).find_one(query)
    elif query_type == "aggregate":
        data = MongoDB._get_collection(collection_name=collection_name).aggregate(query)
    return data

