from pydantic import BaseModel
from app.serializers.inputs_serializer import InputsSerializer


class HandlerSerializer(BaseModel):
    body: InputsSerializer

    class Config:
        allow_population_by_field_name = True
