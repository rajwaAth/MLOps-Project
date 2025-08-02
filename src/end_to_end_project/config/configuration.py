from end_to_end_project.constants import *  # (CONFIG_FILE_PATH, PARAMS_FILE_PATH, SCHEMA_FILE_PATH)
from end_to_end_project.utils.common import read_yaml, create_directories
from end_to_end_project.entity.config_entity import DataIngestionConfig, DataValidationConfig, DataTransformationConfig, ModelTrainingConfig


class ConfigurationManager:
    def __init__(
        self,
        config_filepath = CONFIG_FILE_PATH,
        params_filepath = PARAMS_FILE_PATH,
        schema_filepath = SCHEMA_FILE_PATH
    ):
    
        self.config = read_yaml(config_filepath)
        self.params = read_yaml(params_filepath)
        self.schema = read_yaml(schema_filepath)

        create_directories([self.config.artifacts_root])

    def get_data_ingestion_config(self) -> DataIngestionConfig:
        config = self.config.data_ingestion

        create_directories([config.root_dir])

        data_ingestion_config = DataIngestionConfig(
            root_dir = config.root_dir,
            source_url = config.source_url,
            local_data_file = config.local_data_file,
            unzip_dir = config.unzip_dir
        )

        return data_ingestion_config

    def get_data_validation_config(self) -> DataValidationConfig:
        config = self.config.data_validation
        schema = self.schema.COLUMNS

        create_directories([config.root_dir])

        data_validation_config = DataValidationConfig(
            root_dir = Path(config.root_dir),
            unzip_data_dir = Path(config.unzip_data_dir),
            STATUS_FILE = config.STATUS_FILE,
            all_schema = schema
        )

        return data_validation_config
    
    def get_data_transformation_config(self) -> DataTransformationConfig:
        config = self.config.data_transformation

        create_directories([config.root_dir])

        data_transformation_config = DataTransformationConfig(
            root_dir = Path(config.root_dir),
            data_path = Path(config.data_path)
        )

        return data_transformation_config
    
    def get_model_training_config(self) -> ModelTrainingConfig:
        config = self.config.model_training
        params = self.params.ElasticNet
        schema = self.schema.TARGET_COLUMN

        create_directories([config.root_dir])

        model_training_config = ModelTrainingConfig(
            root_dir = Path(config.root_dir),
            data_train_path= Path(config.data_train_path),
            data_test_path= Path(config.data_test_path),
            model_name = config.model_name,
            alpha= params.alpha,
            l1_ratio= params.l1_ratio,
            target_column= schema.name

        )

        return model_training_config
    