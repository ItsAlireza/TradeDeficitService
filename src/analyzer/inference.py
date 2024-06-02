from analyzer.models import Models
from analyzer.model_config import model_config
from analyzer.model_loader import ModelLoader


model_loader = ModelLoader(config=model_config)
models = Models(model_loader.loaded_models)


def inference(x):
    x_year = x['year']
    x.drop(['year'], axis=1, inplace=True)

    try:
        detrended_x = models.detrender_predict(x, x_year)
        x = models.clusterer_predict(x, detrended_x)
        pca_results = models.dim_reducer_predict(x)
        pca_results['year'] = x_year
        yhat = models.predictor_predict(pca_results)

    except Exception as e:
        raise RuntimeError(f"An error occurred during inference: {str(e)}")

    return yhat
