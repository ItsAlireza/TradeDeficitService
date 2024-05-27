from pydantic import BaseModel
from app.serializers.inference_serializer import InferenceSerializer


class InputsSerializer(BaseModel):
    inputs: InferenceSerializer

    class Config:
        allow_population_by_field_name = True
