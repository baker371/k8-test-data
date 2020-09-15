"""
class for storage services - Minio and S3
"""
from minio_service import MinioService


class StorageService(MinioService):

    def __init__(self, url, access_key, secret_key):
        self.url = url
        self.access_key = access_key
        self.secret_key = secret_key
        super().__init__(url, access_key, secret_key)

