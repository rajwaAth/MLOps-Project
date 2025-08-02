from dataclasses import dataclass
from pathlib import Path

@dataclass(frozen=True)
class DataIngestionConfig:
    root_dir: Path
    source_url: str
    local_data_file: Path
    unzip_dir: Path

@dataclass(frozen=True)
class DataValidationConfig:
    root_dir:Path
    unzip_data_dir:Path
    STATUS_FILE:str
    all_schema: dict

@dataclass(frozen=True)
class DataTransformationConfig:
    root_dir: Path
    data_path: Path

@dataclass(frozen=True)
class ModelTrainingConfig:
    root_dir: Path
    data_train_path: Path
    data_test_path: Path
    model_name: str
    alpha: float
    l1_ratio: float
    target_column: str 

@dataclass(frozen=True)
class ModelEvaluationConfig:
    root_dir: Path
    data_test_path: Path
    model_path: Path
    metric_file: Path
    all_params: dict
    target_col: str