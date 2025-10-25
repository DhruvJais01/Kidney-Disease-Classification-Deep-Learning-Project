import os
import zipfile
import gdown
from cnnClassifier import logger
from cnnClassifier.utils.common import get_size
from cnnClassifier.entity.config_entity import DataIngestionConfig

class DataIngestion:
    def __init__(self, config: DataIngestionConfig):
        self.config = config

    def download_data(self)->None:
        """
        Download data from source
        """
        try:
            dataset_url = self.config.source_URL
            zip_download_dir = self.config.local_data_file
            os.makedirs(os.path.dirname(zip_download_dir), exist_ok=True)
            logger.info(f"Downloading data from {dataset_url} to {zip_download_dir}")

            file_id = dataset_url.split("/")[-2]
            prefix = "https://drive.google.com/uc?export=download&id="
            gdown.download(prefix + file_id, zip_download_dir, quiet=False)
            logger.info(f"Data downloaded successfully to {zip_download_dir}")
        except Exception as e:
            raise e

    def extract_zip_data(self)->None:
        """
        Extract zip file to the specified directory
        Function returns None
        """
        try:
            unzip_dir = self.config.unzip_dir
            os.makedirs(os.path.dirname(unzip_dir), exist_ok=True)
            with zipfile.ZipFile(self.config.local_data_file, 'r') as zip_ref:
                zip_ref.extractall(unzip_dir)
            logger.info(f"Extracted data to {unzip_dir}")
        except Exception as e:
            raise e