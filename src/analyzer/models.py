import pandas as pd
import numpy as np
import functools
import traceback


class Models:
    def __init__(self, loaded_models):
        self.loaded_models = loaded_models

    @staticmethod
    def method_error_handler(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            try:
                return func(*args, **kwargs)
            except Exception as e:
                raise RuntimeError(f"Error in '{func.__name__}': {str(e)}\ntraceback: {traceback.format_exc()}")
        return wrapper

    @method_error_handler
    def detrender_predict(self, input_data, year):
        detrend_models = self.loaded_models['detrend_model']
        output_data = pd.DataFrame()
        for column, model in detrend_models.items():
            index_colummn = year.values.reshape(-1, 1)
            inputed_data = input_data[column]
            trend = model.predict(index_colummn)

            output_data[column] = inputed_data - trend

        return output_data

    @method_error_handler
    def clusterer_predict(self, new_point, detrended_point):
        cluster_centers = self.loaded_models['clusterer_model']
        distances = [np.linalg.norm(detrended_point - center) for center in cluster_centers.T]
        predicted_cluster = np.argmin(distances)

        new_point['ward_cluster_trend_corrected'] = predicted_cluster

    @method_error_handler
    def dim_reducer_predict(self, new_point):
        scaler_model = self.loaded_models['scaler_model']
        pca_model = self.loaded_models['dim_red_model']

        data_scaled = scaler_model.transform(new_point)
        data_pca = pca_model.transform(data_scaled)

        data_pca_df = pd.DataFrame(data_pca, columns=[f"PC{i + 1}" for i in range(data_pca.shape[1])], index=new_point.index)

        X = data_pca_df.iloc[:, :8]
        return X

    @method_error_handler
    def predictor_predict(self, X):
        predictor_model = self.loaded_models['predictor_model']
        return predictor_model.predict(X)
