from cnnClassifier import logger
from cnnClassifier.pipeline.stage_01_data_ingestion import DataIngestionTrainingPipeline
from cnnClassifier.pipeline.stage_02_prepare_base_model import (
    PrepareBaseModelTrainingPipeline,
)

if __name__ == "__main__":
    try:
        logger.info("\n\n>>>>> Stage 01 started <<<<<\n\n")
        data_ingestion = DataIngestionTrainingPipeline()
        data_ingestion.main()

        logger.info("\n\n>>>>> Stage 02 started <<<<<\n\n")
        prepare_base_model = PrepareBaseModelTrainingPipeline()
        prepare_base_model.main()

    except Exception as e:
        logger.exception(e)
        raise e
