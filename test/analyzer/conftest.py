import pytest
from published.test.app.factory.inference_serializer_factory import InferenceSerializerFactory
import numpy as np
import pandas as pd


@pytest.fixture
def fixture_return_valid_input(mocker):
    valid_input = InferenceSerializerFactory().build().dict()
    return pd.DataFrame(valid_input, index=[0])


@pytest.fixture
def fixture_models_work_without_errors(mocker):
    sample_dict = {'year': [2022, 2023, 2024], 'feature1': [1, 2, 3], 'feature2': [4, 5, 6]}

    mocker.patch('analyzer.inference.models.predictor_predict').return_value = np.random.rand(1)
    mocker.patch('analyzer.inference.models.detrender_predict').return_value = pd.DataFrame(sample_dict)
    mocker.patch('analyzer.inference.models.clusterer_predict').return_value = pd.DataFrame(sample_dict)
    mocker.patch('analyzer.inference.models.dim_reducer_predict').return_value = pd.DataFrame(sample_dict)


@pytest.fixture
def fixture_return_invalid_input():
    return pd.DataFrame()


@pytest.fixture
def fixture_models_raise_runtime_error(mocker):
    mocker.patch('analyzer.inference.models.detrender_predict', side_effect=RuntimeError('Error message'))
