import os

from dotenv import load_dotenv

load_dotenv()

COLLECTION_NAME: str = os.getenv("COLLECTION_NAME", "")
MILVUS_HOST: str = os.getenv("MILVUS_HOST", "")
MILVUS_PORT: str = os.getenv("MILVUS_PORT", "")
IMAGE_DIR: str = os.getenv("IMAGE_DIR", "")
