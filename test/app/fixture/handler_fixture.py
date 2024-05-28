import pytest

from test.app.factory.inference_serializer_factory import InferenceSerializerFactory


class HandlerFixtures:
    @pytest.fixture
    def return_valid_input_fixture():
        valid_input = InferenceSerializerFactory().build()
        return {
            'body': {
                'inputs': valid_input.dict(by_alias=True)
            }
        }

    @pytest.fixture
    def return_invalid_json_fixture():
        return {
            'body': 'Invalid JSON'
        }

    @pytest.fixture
    def return_invalid_model_input_fixture():
        invalid_input = InferenceSerializerFactory().build()
        invalid_input.year = 'invalid_year'  # Create a model validation error
        return {
            'body': {
                'inputs': invalid_input.dict(by_alias=True)
            }
        }

    @pytest.fixture
    def inference_error_fixture(mocker):
        mocker.patch('published.analyzer.inference.inference', side_effect=Exception('Inference error'))
        return {
            'body': {
                'inputs': InferenceSerializerFactory().build().dict(by_alias=True)
            }
        }