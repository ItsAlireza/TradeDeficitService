import json
import pandas as pd
from published.analyzer.inference import inference
from app.serializers.inference_serializer import InferenceSerializer
from pydantic import ValidationError
from . import DEBUG


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
        x = pd.DataFrame([inputs_model.__dict__])
    except ValidationError as e:
        return {
            'statusCode': 400,
            'body': e.json()
        }

    try:
        res = inference(x)
        result = int(res[0])

        return {
            'statusCode': 200,
            'body': json.dumps({'predicted trade deficit is': result})
        }
    except Exception as e:
        error_message = str(e) if DEBUG else 'Internal Server Error'
        return {
            'statusCode': 500,
            'body': json.dumps({'error': error_message})
        }



