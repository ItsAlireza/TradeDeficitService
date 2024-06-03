from analyzer.inference import inference
import pytest


class TestInference:
    @staticmethod
    def test_valid_input_return_200(fixture_return_valid_input, fixture_models_work_without_errors):
        x = fixture_return_valid_input

        response = inference(x)

        assert response.shape == (1,)

    @staticmethod
    def test_model_exception_raises_runtime_error(fixture_return_valid_input, fixture_models_raise_runtime_error):
        x = fixture_return_valid_input

        with pytest.raises(RuntimeError):
            inference(x)

    @staticmethod
    def test_invalid_data_raises_keyerror(fixture_return_invalid_input):
        x = fixture_return_invalid_input

        with pytest.raises(KeyError):
            inference(x)
