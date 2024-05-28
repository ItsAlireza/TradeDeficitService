from pydantic_factories import ModelFactory

from app.serializers.inputs_serializer import InputsSerializer


class InputsSerializerFactory(ModelFactory[InputsSerializer]):
    __model__ = InputsSerializer