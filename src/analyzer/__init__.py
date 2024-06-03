from analyzer.models import Models
from analyzer.model_config import model_config
from analyzer.model_loader import ModelLoader


model_loader = ModelLoader(config=model_config)
models = Models(model_loader.loaded_models)
