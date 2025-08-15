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
        data_transformation = DataTransformation(df=pd.read_csv(data_transformation_config.data_path), config=data_transformation_config)
        data_transformation.run_data_transformation(do_clean=True, do_split=True, do_outliers=False, do_skewness=False, do_imbalanced=False)

if __name__ == "__main__":
    try:
        logger.info(f">>>>>> stage {STAGE_NAME} started <<<<<<")
        obj = DataTransformationPipeline()
        obj.main()
        logger.info(f">>>>>> stage {STAGE_NAME} completed <<<<<<")
    except Exception as e:
        logger.exception(e)
        raise e