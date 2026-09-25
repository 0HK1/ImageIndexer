from pymilvus import DataType, FieldSchema

fields_image = [
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
