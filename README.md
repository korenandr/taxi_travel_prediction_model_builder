# Overview
This repository build travel_time prediction model. You can use this model here:
https://github.com/korenandr/taxi_travel_time_prediction

# How to build model
```bash
docker image build . -t model_builder
docker run --name test_builder -v ~/taxi_travel_prediction_model_builder:/app/src --rm model_builder
```
