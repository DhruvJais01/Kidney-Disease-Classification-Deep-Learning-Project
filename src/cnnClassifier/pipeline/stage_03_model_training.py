from cnnClassifier.config.configuration import ConfigurationManager
from cnnClassifier.components.model_training import Training
from cnnClassifier.utils.common import logger


STAGE_NAME = "Model Training"


class ModelTrainingPipeline:
    def __init__(self):
        pass

    def main(self):
        try:
            config = ConfigurationManager()
            training_config = config.get_traning_config()
            training = Training(config=training_config)
            training.get_base_model()
            training.train_valid_generator()
            training.train()
        except Exception as e:
            raise e


if __name__ == "__main__":
    try:
        logger.info(f"\n\n>>>>> {STAGE_NAME} started <<<<<\n\n")
        obj = ModelTrainingPipeline()
        obj.main()
        logger.info(f"\n\n>>>>> {STAGE_NAME} completed <<<<<\n\n")
    except Exception as e:
        logger.exception(e)
        raise e
