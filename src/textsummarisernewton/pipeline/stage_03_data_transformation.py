import sys
import os

# Add src to the PYTHONPATH
src_path = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..'))
if src_path not in sys.path:
    sys.path.append(src_path)

from textsummarisernewton.config.configuration import ConfigurationManager
from textsummarisernewton.components.data_transformation import DataTransformation
from textsummarisernewton.logging.logger import logger


class DataTransformationTrainingPipeline:
    def __init__(self):
        pass

    def main(self):
        config = ConfigurationManager()
        data_transformation_config = config.get_data_transformation_config()
        data_transformation = DataTransformation(config=data_transformation_config)
        data_transformation.convert()