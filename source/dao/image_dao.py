from client.milvus_client import MilvusClient
from pymilvus import FieldSchema
from pymilvus.orm.mutation import MutationResult
from schema.image_schema import fields_image


class ImageDAO:
    def __init__(
        self, connection: MilvusClient, fields: list[FieldSchema] | None = fields_image
    ) -> None:
        self.fields = fields
        self.connection = connection
        self.connection.fields = self.fields
        self.collection = self.connection.get_collection()

    def set_fields_schema(self, schema: list[FieldSchema]) -> None:
        self.fields = schema

    def insert(self, data: list) -> MutationResult:
        collection = self.collection
        result = collection.insert(data)
        self.collection.flush()
        return result
