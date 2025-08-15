import os
import numpy as np
from end_to_end_project import logger
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import PowerTransformer
from imblearn.over_sampling import SMOTE
import pandas as pd
from end_to_end_project.entity.config_entity import DataTransformationConfig

class DataTransformation:
    def __init__(self, df: pd.DataFrame, config: DataTransformationConfig):
        self.config = config
        self.df = df.copy()

    def clean_data(self) -> pd.DataFrame:
        # Remove rows with missing values
        self.df.dropna(inplace=True)
        # Remove duplicated rows
        self.df.drop_duplicates(inplace=True)
        logger.info(f"Cleaned data shape: {self.df.shape}")
        return self.df
    

    def data_split(self, test_size: float = 0.25, random_state:int = 42):
        train, test = train_test_split(self.df, test_size=test_size, random_state=random_state)
        return train.reset_index(drop=True), test.reset_index(drop=True)

    def handle_outliers(self, train: pd.DataFrame) -> pd.DataFrame:
        numeric_cols = train.select_dtypes(include=np.number).columns.drop('quality')
        condition = pd.Series(True, index=train.index)

        for col in numeric_cols:
            Q1 = train[col].quantile(0.25)
            Q3 = train[col].quantile(0.75)
            IQR = Q3 - Q1
            lower_bound = Q1 - 1.5 * IQR
            upper_bound = Q3 + 1.5 * IQR
            # with iqr
            # condition &= (train[col] >= lower_bound) & (train[col] <= upper_bound)
            # with capping
            train[col] = np.where(train[col] < lower_bound, lower_bound, train[col])
            train[col] = np.where(train[col] > upper_bound, upper_bound, train[col])

        # train = train[condition].reset_index(drop=True)
        train.reset_index(drop=True, inplace=True)

        return train

    def handle_skewness_normalize(self, train: pd.DataFrame, test: pd.DataFrame, skew_threshold: float = 1.0) -> pd.DataFrame:
        numeric_cols = train.select_dtypes(include=[np.number]).columns.drop('quality')
        pt = PowerTransformer(method='yeo-johnson', standardize=True)
        skewed_cols = [col for col in numeric_cols if abs(train[col].skew())>skew_threshold]
        if len(skewed_cols) > 0:
            logger.info(f"Handling skewness for columns:")
            train[skewed_cols] = pt.fit_transform(train[skewed_cols])
            test[skewed_cols] = pt.transform(test[skewed_cols])
        else:
            logger.info("No skewed columns found, skipping normalization.")

        return train,test
    
    def handle_imbalenced(self, train: pd.DataFrame) -> pd.DataFrame:
        X = train.drop('quality', axis=1)
        y = train['quality']

        class_counts = y.value_counts()
        min_samples = class_counts.min()

        if min_samples <= 4:
            smote = SMOTE(random_state=42, k_neighbors=min_samples-1)
            logger.info(f"Minimum sample in any class: {min_samples}")
        elif min_samples >= 5:
            smote = SMOTE(random_state=42)

        X_resampled, y_resampled = smote.fit_resample(X, y)
        train = pd.concat([pd.DataFrame(X_resampled, columns=X.columns), pd.Series(y_resampled, name=y.name)], axis=1)
        return train
    
    def make_result(self, train, test):
        # Save the processed train and test data
        train.to_csv(os.path.join(self.config.root_dir, "train.csv"), index=False)
        test.to_csv(os.path.join(self.config.root_dir, "test.csv"), index=False)
        
        logger.info(f"Processed train and test data saved at {self.config.root_dir}")
        logger.info(f"Train data shape: {train.shape}, Test data shape: {test.shape}")
        
        return train, test

    def run_data_transformation(self, do_clean=True, do_split=True, do_outliers=True, do_skewness=True, do_imbalanced=True):
        if do_clean == True:
            self.clean_data()
        if do_split == True:
            train, test = self.data_split()
        if do_outliers == True:
            train = self.handle_outliers(train)
        if do_skewness == True:
            train, test = self.handle_skewness_normalize(train, test)
        if do_imbalanced == True:
            train = self.handle_imbalenced(train)
        self.make_result(train, test)