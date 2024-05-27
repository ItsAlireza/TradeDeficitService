import json
import pandas as pd
from published.analyzer.inference import inference
from app.serializers.inference_serializer import InferenceSerializer
from pydantic import ValidationError


def handler(event, context):
    try:
        inputs = event['body']['inputs']
    except KeyError:
        return {
            'statusCode': 400,
            'body': json.dumps({'error': 'Invalid JSON in request body'})
        }

    try:
        inputs_model = InferenceSerializer(**inputs)
        x = pd.DataFrame([inputs_model.__dict__])  # Directly create DataFrame
    except ValidationError as e:
        print(e.json())

    res = inference(x)
    result = int(res[0])

    return {
        'statusCode': 200,
        'body': json.dumps({'predicted trade deficit is': result})
    }



