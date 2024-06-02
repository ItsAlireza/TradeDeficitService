import json
import pytest
from app.lambda_function import handler


class TestHandler:
    @staticmethod
    def test_valid_input_return_200(fixture_return_valid_input):
        event = fixture_return_valid_input
        context = {}

        response = handler(event, context)

        assert response['statusCode'] == 200
        assert 'predicted trade deficit is' in json.loads(response['body'])

    @staticmethod
    def test_invalid_body_return_400(fixture_return_invalid_body):
        event = fixture_return_invalid_body
        context = {}

        response = handler(event, context)

        assert response['statusCode'] == 400
        assert json.loads(response['body']) == {'error': 'Invalid request body'}

    @staticmethod
    def test_invalid_inputs_return_400(fixture_return_invalid_model_input):
        event = fixture_return_invalid_model_input
        context = {}

        response = handler(event, context)

        assert response['statusCode'] == 400

    @staticmethod
    @pytest.mark.parametrize("debug_value, expected_error_message", [
        (True, 'Inference error'),
        (False, 'Internal Server Error')
    ])
    def test_inference_error_return_500(mocker, fixture_inference_error, debug_value, expected_error_message):
        mocker.patch('app.lambda_function.DEBUG', debug_value)
        event = fixture_inference_error
        context = {}

        response = handler(event, context)

        assert response['statusCode'] == 500
        assert json.loads(response['body']) == {'error': expected_error_message}
