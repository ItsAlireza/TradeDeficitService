from pydantic_factories import ModelFactory

from app.serializers.handler_serializer import HandlerSerializer


class HandlerSerializerFactory(ModelFactory[HandlerSerializer]):
    __model__ = HandlerSerializer