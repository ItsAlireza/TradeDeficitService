from pydantic_factories import ModelFactory

from app.serializers.inference_serializer import InferenceSerializer


class InferenceSerializerFactory(ModelFactory[InferenceSerializer]):
    __model__ = InferenceSerializer