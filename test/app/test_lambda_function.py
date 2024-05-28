import json
import pytest
from app.lambda_function import handler


@pytest.mark.usefixtures("return_valid_input_fixture", "return_invalid_json_fixture",
                         "return_invalid_model_input_fixture", "inference_error_fixture")
class HandlerTest:
    @staticmethod
    def test_valid_input_return_200(return_valid_input_fixture):
        event = return_valid_input_fixture
        context = {}
        response = handler(event, context)
        assert response['statusCode'] == 200
        assert 'predicted trade deficit is' in json.loads(response['body'])

    @staticmethod
    def test_invalid_json_return_400(return_invalid_json_fixture):
        event = return_invalid_json_fixture
        context = {}
        response = handler(event, context)
        assert response['statusCode'] == 400
        assert json.loads(response['body']) == {'error': 'Invalid JSON in request body'}

    @staticmethod
    def test_invalid_inputs_return_400(return_invalid_model_input_fixture):
        event = return_invalid_model_input_fixture
        context = {}
        response = handler(event, context)
        assert response['statusCode'] == 400

    @staticmethod
    @pytest.mark.parametrize("debug_value, expected_error_message", [
        (True, 'Inference error'),
        (False, 'Internal Server Error')
    ])
    def test_inference_error_return_500(mocker, inference_error_fixture, debug_value, expected_error_message):
        mocker.patch('app.lambda_function.DEBUG', debug_value)
        event = inference_error_fixture
        context = {}
        response = handler(event, context)
        assert response['statusCode'] == 500
        assert json.loads(response['body']) == {'error': expected_error_message}
