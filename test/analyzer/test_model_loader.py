from analyzer.model_loader import ModelLoader
import pytest


class TestModelLoader:
    @staticmethod
    def test_load_models_missing_env_var(mock_path_env_vars, monkeypatch):
        monkeypatch.delenv("MODEL_PATH_VAR", raising=False)

        config = {"model1": "MODEL_PATH_VAR"}

        with pytest.raises(ValueError, match="Environment variable MODEL_PATH_VAR is not set"):
            ModelLoader(config)
