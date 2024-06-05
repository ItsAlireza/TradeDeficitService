from numpy import ndarray
import pandas as pd
from . import models


def inference(x: pd.DataFrame) -> ndarray:
    x_year = x['year']
    x.drop(['year'], axis=1, inplace=True)

    try:
        detrended_x = models.detrender_predict(x, x_year)
        models.clusterer_predict(x, detrended_x)
        pca_results = models.dim_reducer_predict(x)
        pca_results['year'] = x_year
        yhat = models.predictor_predict(pca_results)

    except Exception as e:
        raise RuntimeError(f"An error occurred during inference: \n\n{str(e)}")

    return yhat
