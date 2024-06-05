import pickle
import os
import boto3
from io import BytesIO


class ModelLoader:
    def __init__(self, config):
        self.source = os.getenv('MODEL_SOURCE')
        self.s3_client = boto3.client('s3') if self.source == 's3' else None
        self.loaded_models = {}
        self.load_models(config)

    def load_models(self, config):
        for model_name, path_var in config.items():
            set_path = os.getenv(path_var)
            if not set_path:
                raise ValueError(f"Environment variable {path_var} is not set")

            try:
                if self.source == 'disk':
                    self._load_from_disk(model_name, set_path)
                elif self.source == 's3':
                    self._load_from_s3(model_name, set_path)
                else:
                    raise ValueError(f"Unknown source: {self.source}")
            except Exception as e:
                print(f"An error occurred while loading model {model_name}: {e}")

    def _load_from_disk(self, model_name, set_path):
        full_path = os.path.join(os.getenv("FILEPATH"), set_path)
        try:
            with open(full_path, 'rb') as f:
                self.loaded_models[model_name] = pickle.load(f)
        except FileNotFoundError:
            print(f"File not found for model {model_name} at path {full_path}")

    def _load_from_s3(self, model_name, set_path):
        bucket_name = os.getenv("BUCKET_NAME")
        obj_key = os.getenv("FILEPATH") + '/' + set_path
        try:
            obj = self.s3_client.get_object(Bucket=bucket_name, Key=obj_key)
            buffer = BytesIO(obj['Body'].read())
            self.loaded_models[model_name] = pickle.load(buffer)
        except self.s3_client.exceptions.NoSuchKey:
            print(f"File not found for model {model_name} at S3 path {set_path}")
