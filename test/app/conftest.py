import pytest
from published.test.app.factory.inference_serializer_factory import InferenceSerializerFactory
import numpy as np


@pytest.fixture
def fixture_return_valid_input(mocker):
    mocker.patch('app.lambda_function.inference').return_value = np.random.rand(1)

    valid_input = InferenceSerializerFactory().build()
    return {
        'body': {
            'inputs': valid_input.dict(by_alias=True)
        }
    }


@pytest.fixture
def fixture_return_invalid_body():
    return {
        'body': 'Invalid body'
    }


@pytest.fixture
def fixture_return_invalid_model_input():
    invalid_input = InferenceSerializerFactory().build()
    invalid_input.year = 'invalid_year'
    return {
        'body': {
            'inputs': invalid_input.dict(by_alias=True)
        }
    }


@pytest.fixture
def fixture_inference_error(mocker):
    mocker.patch('app.lambda_function.inference', side_effect=Exception('Inference error'))
    return {
        'body': {
            'inputs': InferenceSerializerFactory().build().dict(by_alias=True)
        }
    }
