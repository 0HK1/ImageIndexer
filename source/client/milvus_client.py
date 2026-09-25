from config.config import COLLECTION_NAME, MILVUS_HOST, MILVUS_PORT
from pymilvus import (
    Collection,
    CollectionSchema,
    FieldSchema,
    connections,
    utility,
)


class MilvusClient:
    def __init__(self, fields: list[FieldSchema] | None = None) -> None:
        self.fields = fields

    def connect(self) -> None:
        connections.connect(
            alias="default",
            host=MILVUS_HOST,
            port=MILVUS_PORT,
        )

    def set_fields(self, fields: list[FieldSchema]) -> None:
        self.fields = fields

    def get_collection(self) -> Collection:

        if utility.has_collection(COLLECTION_NAME):
            return Collection(COLLECTION_NAME)

        if not self.fields:
            raise ValueError("The FieldSchema list cannot be empty.")

        schema = CollectionSchema(
            fields=self.fields, # type: ignore
            description="Image pHash collection",
        )

        collection = Collection(
            name=COLLECTION_NAME,
            schema=schema,
        )

        index_params = {
            "metric_type": "L2",
            "index_type": "IVF_FLAT",
            "params": {
                "nlist": 128,
            },
        }

        collection.create_index(
            field_name="vector",
            index_params=index_params,
        )  # type: ignore

        return collection
