import os
from unittest import TestCase
from storage_service import StorageService


class TestMinioService(TestCase):

    @classmethod
    def setUpClass(cls):
        access_key = os.getenv("ACCESS_KEY")
        secret_key = os.getenv("SECRET_KEY")
        minio_host = os.getenv("STORAGE_HOST")
        cls.minio = StorageService(minio_host, access_key=access_key, secret_key=secret_key)

    def test_create_bucket(self):
        test_bucket_name = "test-bucket"
        self.minio.delete_bucket(test_bucket_name, ignore_if_not_exists=True)
        assert self.minio.create_bucket(test_bucket_name)

    def test_upload_file(self):
        local_file_name = "test_file.txt"
        cwd = os.getcwd()
        full_path = os.path.join(cwd, local_file_name)
        test_bucket_name = "test-bucket"
        assert self.minio.upload_file(test_bucket_name, full_path)

    def test_download_file(self):
        file_name = "test_file.txt"
        test_bucket_name = "test-bucket"
        self.minio.download_file(test_bucket_name, file_name)

    def test_list_buckets(self):
        list_buckets = self.minio.list_buckets()
        assert list_buckets == ["test-bucket"]
