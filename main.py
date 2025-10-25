from cnnClassifier import logger
from cnnClassifier.pipeline.stage_01_data_ingestion import DataIngestionTrainingPipeline

if __name__ == "__main__":
    try:
        logger.info("Starting the main function")
        obj = DataIngestionTrainingPipeline()
        obj.main()
        logger.info("Completed the main function")
    except Exception as e:
        logger.exception(e)
        raise e
