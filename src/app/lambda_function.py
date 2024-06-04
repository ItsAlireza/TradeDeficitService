import json
import pandas as pd
from analyzer.inference import inference
from app.serializers.inference_serializer import InferenceSerializer
from pydantic import ValidationError
from . import DEBUG, logger


def handler(event, context):
    try:
        body = event['body']
        if not isinstance(body, dict):
            raise ValueError

        inputs = body['inputs']
    except (KeyError, ValueError):
        return {
            'statusCode': 400,
            'body': json.dumps({'error': str("Invalid request body")})
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
        result = inference(x)
        return {
            'statusCode': 200,
            'body': json.dumps({'predicted trade deficit is': result[0]})
        }

    except Exception as e:
        logger.exception(extra={'inputs': inputs_model})
        error_message = str(e) if DEBUG else 'Internal Server Error'
        return {
            'statusCode': 500,
            'body': json.dumps({'error': error_message})
        }
