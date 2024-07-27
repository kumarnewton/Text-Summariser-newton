<<<<<<< HEAD
from src.textsummarisernewton.pipeline.stage_01_data_ingestion import DataIngestionTrainingPipeline
from src.textsummarisernewton.logging.logger import logger 


STAGE_NAME = "data Ingestion stage"
try:
    logger.info(f">>>>>> stage {STAGE_NAME} started <<<<<<")
    data_ingestion = DataIngestionTrainingPipeline()
    data_ingestion.main()
    logger.info(f">>>>>> stage {STAGE_NAME} completed <<<<<<\n\nx==========x")
except Exception as e:
    logger.exception(e)
    raise e
=======
from src.textSummarisernewton.logging import logger

logger.info("Welcome to our custom logging")

def main():
    logger.info("This is the main function")

if _name_ == "_main_":
main()
>>>>>>> ca1bb869cf8c927b3717915e68f205b2c978bb11
