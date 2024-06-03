import pickle
import os


class ModelLoader:
    def __init__(self, config):
        self.loaded_models = {}
        self.load_models(config)

    def load_models(self, config):
        files_path = os.getenv("FILEPATH")
        for model_name, path_var in config.items():
            set_path = os.getenv(path_var)
            if not set_path:
                raise ValueError(f"Environment variable {path_var} is not set")

            full_path = os.path.join(files_path, set_path)

            try:
                with open(full_path, 'rb') as f:
                    self.loaded_models[model_name] = pickle.load(f)
            except FileNotFoundError:
                print(f"File not found for model {model_name} at path {full_path}")
            except Exception as e:
                print(f"An error occurred while loading model {model_name}: {e}")
