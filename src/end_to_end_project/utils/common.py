import os 
from box.exceptions import BoxValueError
import yaml
from end_to_end_project import logger
import json
import joblib
from typeguard import typechecked
from box import ConfigBox
from pathlib import Path
from typing import Any


@typechecked
def read_yaml(path_to_yaml: Path) -> ConfigBox:
    """
    Reads a YAML file and returns a ConfigBox
    
    Args:
        path_to_yaml (Path): Path to the YAML file
    
    Returns:
        ConfigBox: ConfigBox containing the YAML data
    """
    try:
        with open(path_to_yaml) as yaml_file:
            content = yaml.safe_load(yaml_file)
            logger.info(f"YAML file: {path_to_yaml} loaded successfully")
            return ConfigBox(content)
    except BoxValueError:
        raise ValueError(f"YAML file is empty")
    except Exception as e:
        raise e
    
@typechecked
def  create_directories(path_to_directories: list, verbose=True):
    """
    Create list of directories

    Args:
        path_to_directories (List): List of path of directories
        ignore_log (bool, optional): Ignore if multiple directories are created. Defaults to False
    """

    for path in path_to_directories:
        os.makedirs(path, exist_ok=True)
        if verbose:
            logger.info(f"Created directory at: {path}")

@typechecked
def save_json(path: Path, data: dict):
    """
    Save data to a JSON file

    Args:
        path (Path): Path to save the JSON file
        data (dict): Data to be saved
    """
    with open(path, 'w') as f:
        json.dump(data, f, indent=4)
    logger.info(f"JSON file saved at: {path}")

@typechecked
def load_json(path: Path) -> ConfigBox:
    """
    Load data from a JSON file

    Args:
        path (Path): Path to the JSON file

    Returns:
        ConfigBox: Data as class attributes instead of dict
    """
    with open(path, 'r') as f:
        data = json.load(f)

    logger.info(f"Json file loaded succsessfully from: {path}")
    return ConfigBox(data)

@typechecked
def save_bin(data: Any, path: Path):
    """
    Save binary file

    Args:
        data (Any): data to be saved as binary
        path (Path): path to save the binary file
    """
    joblib.dump(value=data, filename=path)
    logger.info(f"Binary file saved at: {path}")

@typechecked
def load_bin(path: Path) -> Any:
    """
    Load binary file

    Args:
        path (Path): path to the binary file

    Returns:
        Any: data loaded from the binary file
    """
    data = joblib.load(filename=path)
    logger.info(f"Binary file loaded successfully from: {path}")
    return data

@typechecked
def get_size(path: Path) -> str:
    """
    Get size of file

    Args:
        path (Path): path to the file

    Returns:
        int: size of the file in bytes
    """
    size_in_kb = os.path.getsize(path) / 1024
    return f"{size_in_kb} KB"