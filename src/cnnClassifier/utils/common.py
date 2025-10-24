import os
from box.exceptions import BoxValueError
import yaml
from cnnClassifier import logger
import json
import joblib
from ensure import ensure_annotations
from box import ConfigBox
from pathlib import Path
from typing import Any
import base64

@ensure_annotations
def read_yaml(path_to_yaml: Path) -> ConfigBox:
    """Reads a YAML file and returns the content as a ConfigBox object.

    Args:
        path_to_yaml (Path): Path to the YAML file.

    Returns:
        ConfigBox: ConfigBox object containing the content of the YAML file."""


    try:
        with open(path_to_yaml, 'r') as yaml_file:
            content = yaml.safe_load(yaml_file)
            logger.info(f"YAML file loaded successfully: {path_to_yaml}")
            return ConfigBox(content)
    except BoxValueError:
        raise ValueError("YAML file is empty")
    except Exception as e:
        raise e

@ensure_annotations
def create_directories(path_to_directories: list, verbose=True):
    """Create directories from a list of paths.

    Args:
        path_to_directories (list): List of paths to directories.
        verbose (bool, optional): Whether to log verbose output. Defaults to True."""
    try:
        for path in path_to_directories:
            os.makedirs(path, exist_ok=True)
            if verbose:
                logger.info(f"Directory created successfully: {path}")
    except Exception as e:
        raise e 
        
@ensure_annotations
def save_json(path: Path, data: dict):
    """Save a dictionary as a JSON file.

    Args:
        path (Path): Path to the JSON file.
        data (dict): Dictionary to save as JSON."""
    try:
        with open(path, 'w') as json_file:
            json.dump(data, json_file, indent=4)
            logger.info(f"JSON file saved successfully: {path}")
    except Exception as e:
        raise e

@ensure_annotations
def load_json(path: Path) -> ConfigBox:
    """Load a JSON file and return the content as a ConfigBox object.

    Args:
        path (Path): Path to the JSON file.

    Returns:
        ConfigBox: ConfigBox object containing the content of the JSON file."""
    try:
        with open(path, 'r') as json_file:
            data = json.load(json_file)
            logger.info(f"JSON file loaded successfully: {path}")
            return ConfigBox(data)
    except Exception as e:
        raise e

@ensure_annotations
def save_bin(data: Any, path: Path):
    """Save an object as a binary file.

    Args:
        data (Any): Object to save as binary.
        path (Path): Path to the binary file."""
    try:
        joblib.dump(data, path)
        logger.info(f"Binary file saved successfully: {path}")
    except Exception as e:
        raise e

@ensure_annotations
def load_bin(path: Path) -> Any:
    """Load a binary file and return the content as an object.

    Args:
        path (Path): Path to the binary file.

    Returns:
        Any: Object loaded from the binary file."""
    try:
        data = joblib.load(path)
        logger.info(f"Binary file loaded successfully: {path}")
        return data
    except Exception as e:
        raise e

@ensure_annotations
def get_size(path: Path) -> str:
    """Get the size of a file in bytes.

    Args:
        path (Path): Path to the file.

    Returns:
        str: Size of the file in bytes."""
    try:
        size = os.path.getsize(path)
        logger.info(f"File size: {size} bytes")
        return size
    except Exception as e:
        raise e

@ensure_annotations
def decodeImage(imgString: str, fileName: str):
    """Decode an image from a base64 string and save it as a file.

    Args:
        imgString (str): Base64 string of the image.
        fileName (str): Name of the file to save the image as."""
    try:
        imgdata = base64.b64decode(imgString)
        with open(fileName, 'wb') as f:
            f.write(imgdata)
            f.close()
        logger.info(f"Image decoded successfully: {fileName}")

    except Exception as e:
        raise e

@ensure_annotations
def encodeImageIntoBase64(croppedImagePath: str) -> str:
    """Encode an image into a base64 string.

    Args:
        croppedImagePath (str): Path to the image to encode.

    Returns:
        str: Base64 string of the image."""
    try:
        with open(croppedImagePath, "rb") as f:
            encoded_string = base64.b64encode(f.read())
        logger.info("Image encoded successfully")
        return encoded_string
    except Exception as e:
        raise e