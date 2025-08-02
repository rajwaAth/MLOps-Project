import os
import pandas as pd
from sklearn.metrics import mean_squared_error, mean_absolute_error, r2_score
from urllib.parse import urlparse
from dagshub import init
import mlflow
import mlflow.sklearn
import numpy as np
import joblib
from end_to_end_project.utils.common import save_json
from end_to_end_project.entity.config_entity import ModelEvaluationConfig
from pathlib import Path

class ModelEvaluation:
    def __init__(self, config: ModelEvaluationConfig):
        self.config = config
        init(repo_owner="rajwaAth", repo_name='MLOps-Project', mlflow=True)

    def eval_metrics(self, actual, pred):
        rmse = np.sqrt(mean_squared_error(actual, pred))
        mae = mean_absolute_error(actual, pred)
        r2 = r2_score(actual, pred)
        return rmse, mae, r2
    
    def log_into_mlflow(self):
        test_data = pd.read_csv(self.config.data_test_path)
        model = joblib.load(self.config.model_path)

        X_test = test_data.drop(columns=[self.config.target_col])
        y_test = test_data[self.config.target_col]

        pred = model.predict(X_test)
        rmse, mae, r2 = self.eval_metrics(y_test, pred)

        scores = {
            "rmse": rmse,
            "mae": mae,
            "r2": r2
        }
        save_json(path=Path(self.config.metric_file), data=scores)

        with mlflow.start_run():
            mlflow.log_params(self.config.all_params)
            for key, value in scores.items():
                mlflow.log_metric(key, value)
            mlflow.sklearn.log_model(model, "model", registered_model_name="ElasticNetModel")



