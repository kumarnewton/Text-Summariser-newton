import sys
import os

# Add src to the PYTHONPATH
src_path = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..'))
if src_path not in sys.path:
    sys.path.append(src_path)

from textsummarisernewton.config.configuration import ConfigurationManager
from textsummarisernewton.components.data_validation import DataValidation
from textsummarisernewton.logging.logger import logger

class DataValidationTrainingPipeline:
    def __init__(self):
        pass

    def main(self):
        config = ConfigurationManager()
        data_validation_config = config.get_data_validation_config()  # Ensure this method returns DataValidationConfig
        data_validation = DataValidation(config=data_validation_config)
        data_validation.validate_all_files_exist()