import pandas as pd
import os
from end_to_end_project import logger
import joblib
from sklearn.linear_model import ElasticNet
from end_to_end_project.entity.config_entity import ModelTrainingConfig

class ModelTraining:
    def __init__(self, config: ModelTrainingConfig):
        self.config = config

    def train_model(self):
        train_data = pd.read_csv(self.config.data_train_path)
        test_data = pd.read_csv(self.config.data_test_path)

        X_train = train_data.drop([self.config.target_column], axis=1)
        y_train = train_data[self.config.target_column]
        X_test = test_data.drop([self.config.target_column], axis=1)
        y_test = test_data[self.config.target_column]

        model = ElasticNet(
            alpha=self.config.alpha,
            l1_ratio=self.config.l1_ratio,
            random_state=42
        )
        model.fit(X_train, y_train)

        joblib.dump(model, os.path.join(self.config.root_dir, self.config.model_name))