from cnnClassifier.config.configuration import ConfigurationManager
from cnnClassifier.components.model_evaluation_mlflow import Evaluation
from cnnClassifier.utils.common import logger


STAGE_NAME = "Model Evaluation"


class EvaluationPipeline:
    def __init__(self):
        pass

    def main(self):
        try:
            config = ConfigurationManager()
            evaluation_config = config.get_evaluate_config()
            evaluation = Evaluation(config=evaluation_config)
            evaluation.evaluate()
            evaluation.log_into_mlflow()
        except Exception as e:
            raise e


if __name__ == "__main__":
    try:
        logger.info(f"\n\n>>>>> {STAGE_NAME} started <<<<<\n\n")
        obj = EvaluationPipeline()
        obj.main()
        logger.info(f"\n\n>>>>> {STAGE_NAME} completed <<<<<\n\n")
    except Exception as e:
        logger.exception(e)
        raise e
