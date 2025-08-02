import os
from end_to_end_project import logger
from sklearn.model_selection import train_test_split
import pandas as pd
from end_to_end_project.entity.config_entity import DataTransformationConfig

class DataTransformation:
    def __init__(self, config: DataTransformationConfig):
        self.config = config

    def train_test_split(self, df: pd.DataFrame, test_size: float = 0.25, random_state:int = 42):
        data = df.copy()

        train, test = train_test_split(data, test_size=test_size, random_state=random_state)
        train.to_csv(os.path.join(self.config.root_dir, "train.csv"), index = False )
        test.to_csv(os.path.join(self.config.root_dir, "test.csv"), index = False )

        logger.info(f"Train and test data saved at {self.config.root_dir}")
        logger.info(f"Train data shape: {train.shape}, Test data shape: {test.shape}")
        