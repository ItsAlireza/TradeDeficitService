# TradeDeficitService

[![GitHub issues](https://img.shields.io/github/issues/ItsAlireza/TradeDeficitService)](https://github.com/ItsAlireza/TradeDeficitService/issues)
[![GitHub license](https://img.shields.io/github/license/ItsAlireza/TradeDeficitService)](https://github.com/ItsAlireza/TradeDeficitService/blob/main/LICENSE)
[![GitHub stars](https://img.shields.io/github/stars/ItsAlireza/TradeDeficitService)](https://github.com/ItsAlireza/TradeDeficitService/stargazers)

This project explores the dataset gathered for the paper, "Empirical analysis of Marshall-Lerner Condition", which focuses on testing the Marshall-Lerner condition between the United States and Canada. In the paper, Error Correction Models were used to examine the short-run and long-run effects of changes in real exchange rates, and the evidance for both the ML condition and the J-curve.  
I've expanded the features used since violations of most of the classical assumptions are not going to cause a problem for prediction puposes. The goal is to utilize machine learning and unsupervied methods to predict the US budget deficit with Canada and deploy it with AWS (Lambda, S3, and CloudWatch) and Docker.

## Directory Structure

### src
- **App**: Contains files related to the Lambda function.
- **Analyzer**: Responsible for loading the data and performing inference.
- **Notebooks**: Includes Jupyter notebooks for data exploration, clustering, and analysis.
  - **clustering**: The ability of hierarchical and partitional clustering algorithms on both raw and detrended data is examined. Thereafter, the economic intuition is discussed based on the derived clusters.
  - **dimentionality reduction**: As a necessary step, since the annual data is small relative to the number of features. 
### test
- **Unit Tests**: Contains tests for the files in the App directory.
