from cnnClassifier import logger
from cnnClassifier.pipeline.stage_01_data_ingestion import DataIngestionTrainingPipeline
from cnnClassifier.pipeline.stage_02_prepare_base_model import (
    PrepareBaseModelTrainingPipeline,
)
from cnnClassifier.pipeline.stage_03_model_training import ModelTrainingPipeline

if __name__ == "__main__":
    logger.info("\n" + "%" * 100)
    try:
        logger.info("\n\n>>>>> Stage 01 started <<<<<\n\n")
        data_ingestion = DataIngestionTrainingPipeline()
        data_ingestion.main()

        logger.info("\n\n>>>>> Stage 02 started <<<<<\n\n")
        prepare_base_model = PrepareBaseModelTrainingPipeline()
        prepare_base_model.main()

        logger.info("\n\n>>>>> Stage 03 started <<<<<\n\n")
        model_training = ModelTrainingPipeline()
        model_training.main()

    except Exception as e:
        logger.exception(e)
        raise e
    logger.info("\n" + "%" * 100)
