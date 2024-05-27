from published.analyzer.models import Models
from published.analyzer.model_config import model_config
from published.analyzer.model_loader import ModelLoader


model_loader = ModelLoader(config=model_config)
models = Models(model_loader.loaded_models)


def inference(x):
    new_point_year = x['year']
    new_point = x.drop(['year'], axis=1)

    detrended_point = models.detrender_predict(new_point, new_point_year)
    new_point = models.clusterer_predict(new_point, detrended_point)
    pca_results = models.dim_reducer_predict(new_point)
    pca_results['year'] = new_point_year
    yhat = models.predictor_predict(pca_results)

    return yhat
