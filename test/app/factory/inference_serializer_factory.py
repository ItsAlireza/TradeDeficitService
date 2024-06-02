from pydantic_factories import ModelFactory
from src.app.serializers.inference_serializer import InferenceSerializer


class InferenceSerializerFactory(ModelFactory[InferenceSerializer]):
    __model__ = InferenceSerializer
