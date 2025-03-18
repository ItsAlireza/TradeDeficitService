import pickle
import os
import boto3
from io import BytesIO
from abc import ABC, abstractmethod


class ModelLoader:
    """The product class that holds the loaded models."""
    def __init__(self):
        self.loaded_models = {}

    def get_model(self, model_name):
        return self.loaded_models.get(model_name)

    def add_model(self, model_name, model):
        self.loaded_models[model_name] = model


class ModelLoaderBuilder(ABC):
    """Abstract builder for model loaders."""
    def __init__(self):
        self.model_loader = ModelLoader()

    @abstractmethod
    def configure_client(self):
        pass

    @abstractmethod
    def load_model(self, model_name, path):
        pass

    def get_result(self):
        return self.model_loader


class DiskModelLoaderBuilder(ModelLoaderBuilder):
    def configure_client(self):
        pass

    def load_model(self, model_name, path):
        full_path = os.path.join(os.getenv("FILEPATH"), path)
        try:
            with open(full_path, 'rb') as f:
                model = pickle.load(f)
                self.model_loader.add_model(model_name, model)
        except FileNotFoundError:
            print(f"File not found for model {model_name} at path {full_path}")
        return self


class S3ModelLoaderBuilder(ModelLoaderBuilder):
    def configure_client(self):
        self.s3_client = boto3.client('s3')
        return self

    def load_model(self, model_name, path):
        bucket_name = os.getenv("BUCKET_NAME")
        obj_key = os.getenv("FILEPATH") + '/' + path
        try:
            obj = self.s3_client.get_object(Bucket=bucket_name, Key=obj_key)
            buffer = BytesIO(obj['Body'].read())
            model = pickle.load(buffer)
            self.model_loader.add_model(model_name, model)
        except self.s3_client.exceptions.NoSuchKey:
            print(f"File not found for model {model_name} at S3 path {path}")
        return self


class ModelLoaderDirector:
    def __init__(self, source='disk'):
        self.source = source
        self.builder = self._get_builder()
        self.builder.configure_client()

    def _get_builder(self):
        if self.source == 'disk':
            return DiskModelLoaderBuilder()
        elif self.source == 's3':
            return S3ModelLoaderBuilder()
        else:
            raise ValueError(f"Unknown source: {self.source}")

    def construct(self, config):
        """Construct the ModelLoader with the given configuration."""
        for model_name, path_var in config.items():
            set_path = os.getenv(path_var)
            if not set_path:
                raise ValueError(f"Environment variable {path_var} is not set")

            try:
                self.builder.load_model(model_name, set_path)
            except Exception as e:
                print(f"An error occurred while loading model {model_name}: {e}")

        return self.builder.get_result()
