from config.config import (
    COLLECTION_NAME,
    MILVUS_HOST,
    MILVUS_PORT,
)
from pymilvus import (
    Collection,
    CollectionSchema,
    DataType,
    FieldSchema,
    connections,
    utility,
)


def connect() -> None:
    connections.connect(
        alias="default",
        host=MILVUS_HOST,
        port=MILVUS_PORT,
    )


def create_collection(drop_existing: bool = False) -> Collection:

    if drop_existing and utility.has_collection(COLLECTION_NAME):
        utility.drop_collection(COLLECTION_NAME)  # type: ignore

    if utility.has_collection(COLLECTION_NAME):
        return Collection(COLLECTION_NAME)

    fields = [
        FieldSchema(
            name="id",
            dtype=DataType.INT64,
            is_primary=True,
            auto_id=True,
        ),
        FieldSchema(
            name="image_path",
            dtype=DataType.VARCHAR,
            max_length=500,
        ),
        FieldSchema(
            name="phash",
            dtype=DataType.VARCHAR,
            max_length=64,
        ),
        FieldSchema(
            name="vector",
            dtype=DataType.FLOAT_VECTOR,
            dim=64,
        ),
    ]

    schema = CollectionSchema(
        fields=fields,
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
