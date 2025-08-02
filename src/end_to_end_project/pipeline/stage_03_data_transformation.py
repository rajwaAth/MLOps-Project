from end_to_end_project.config.configuration import ConfigurationManager
from end_to_end_project.components.data_transformation import DataTransformation
from end_to_end_project import logger
import pandas as pd

STAGE_NAME = "Data Transformation"

class DataTransformationPipeline:
    def __init__(self):
        pass

    def main(self):
        config = ConfigurationManager()
        data_transformation_config = config.get_data_transformation_config()
        data_transformation = DataTransformation(config=data_transformation_config)
        data_transformation.train_test_split(
            df = pd.read_csv(data_transformation_config.data_path),
            test_size= 0.25,
            random_state= 42)
        
if __name__ == "__main__":
    try:
        logger.info(f">>>>>> stage {STAGE_NAME} started <<<<<<")
        obj = DataTransformationPipeline()
        obj.main()
        logger.info(f">>>>>> stage {STAGE_NAME} completed <<<<<<")
    except Exception as e:
        logger.exception(e)
        raise e