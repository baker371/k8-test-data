import os
from src.minio_service import Minio


class FileService:

    UPLOAD_DIR = os.environ.get("STATIC_PATH", "src/static")

    @staticmethod
    def save_file(file):
        # To Do :  to be replaced by minio file save service
        d = FileService.UPLOAD_DIR
        if not os.path.exists(d):
            os.makedirs(d)
        path = f"{d}/{file.filename}"
        file.save(path)
        return path

    @staticmethod
    def save_to_minio(file):
        file_path = os.path.dirname(file.filename)
        file_name = file.filename.split("/")[-1]
        file_exention = file_name.split(".")[-1]
        url = os.getenv('MINIO_URL')
        access_key = os.getenv('MINIO_ACCESS_KEY')
        secret_key = os.getenv('MINIO_SECRET_KEY')
        minio = Minio(url, access_key, secret_key)
        return minio.upload_to_minio(file_path, file_exention, file_name)
