# TradeDeficitService

[![GitHub issues](https://img.shields.io/github/issues/ItsAlireza/TradeDeficitService)](https://github.com/ItsAlireza/TradeDeficitService/issues)
[![GitHub license](https://img.shields.io/github/license/ItsAlireza/TradeDeficitService)](https://github.com/ItsAlireza/TradeDeficitService/blob/main/LICENSE)
[![GitHub stars](https://img.shields.io/github/stars/ItsAlireza/TradeDeficitService)](https://github.com/ItsAlireza/TradeDeficitService/stargazers)

This project explores the dataset gathered for the paper, *Empirical analysis of Marshall-Lerner Condition*, which focuses on testing the Marshall-Lerner condition between the United States and Canada. In the paper, Error Correction Models were used to examine the short-run and long-run effects of changes in real exchange rates, and the evidence for both the ML condition and the J-curve. 

I've expanded the features used since violations of most of the classical assumptions are not going to cause a problem for prediction purposes. The goal is to utilize machine learning and unsupervised methods to predict the US budget deficit with Canada and deploy it with AWS (Lambda, S3, and CloudWatch) and Docker.

## Directory Structure

### `src`
- **App**: Contains files related to the Lambda function.
- **Analyzer**: Responsible for loading the data and performing inference.
- **Notebooks**: Includes Jupyter notebooks for data exploration, clustering, and analysis.
  - **clustering**: The ability of hierarchical and partitional clustering algorithms on both raw and detrended data is examined. Thereafter, the economic intuition is discussed based on the derived clusters.
  - **dimensionality reduction**: As a necessary step, since the annual data is small relative to the number of features.
  - **modeling**: Comparison of results across multiple algorithms. *note, this notebook is not finalized yet.*
### `test`
- **Unit Tests**: Contains tests for the files in the App directory.


## Setup 

There are several environment variables that should be set.
For the unit tests, they are loaded in `conftest.py` using `.env` files in the `test` directory
For both development and production, they are set in the Dockerfiles accordingly.



### Environment Variables

Several environment variables need to be set for this project. 
They are loaded depending on the context (unit tests, development, or production). 

- **For Unit Tests**: Unit tests load environment variables from `.env` files located in the `test` directory, managed by `conftest.py`. 
- **For Development and Production**: In both development and production environments, these variables are configured within the respective Dockerfiles.
In both development and production environments, these variables are configured within the respective Dockerfiles.

<br>
Below are the environment variables you need to set, and their descriptions:  
<br><br>

**Common variables**

| Variable              | Description                                                           |
|-----------------------|-----------------------------------------------------------------------|
| `DEBUG`               | Set to `true` to return descriptive internal errors                   |
| `MODEL_SOURCE`        | Specifies the source of the model files (`s3` or `disk`).             |
| `FILEPATH`            | The path to the resources root, within the bucket or on disk.         |

<br>

**Model paths**  

`ModelLoader` locates the pretrained models by concatenating the resources root with the full path from the 
resources root to the `.pkl` files. Here are the list of models' paths that should be set:  


| Variable              | Description                               |
|-----------------------|-------------------------------------------|
| `DETREND_PATH`        | Path to the detrend model dictionary.     |
| `CLUSTER_CENTERS_PATH`| Path to the cluster centroids/clustroids. |
| `DIM_RED_PATH`        | Path to the dimension reduction model     |
| `SCALER_PATH`         | Path to the scaler model.                 |
| `PREDICTOR_PATH`      | Path to the final predictor model         |

<br>

### AWS IAM Policy 

The script needs read permission to 
the corresponding bucket attached to the respective role for the lambda function.  

```json
{
    "Version": "2012-10-17",
    "Statement": [
        {
            "Effect": "Allow",
            "Action": [
                "s3:GetObject",
                "s3:ListBucket"
            ],
            "Resource": [
                "arn:aws:s3:::YOUR_BUCKET_NAME",
                "arn:aws:s3:::YOUR_BUCKET_NAME/*"
            ]
        }
    ]
}
```

