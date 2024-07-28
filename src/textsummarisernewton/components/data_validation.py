import sys
import os

# Add src to the PYTHONPATH
src_path = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..'))
if src_path not in sys.path:
    sys.path.append(src_path)

from textsummarisernewton.logging.logger import logger
from textsummarisernewton.entity import DataValidationConfig

class DataValidation:
    def __init__(self, config: DataValidationConfig):
        self.config = config

    def validate_all_files_exist(self) -> bool:
        try:
            all_files = os.listdir(os.path.join("artifacts", "data_ingestion", "samsum_dataset"))
            missing_files = [file for file in self.config.ALL_REQUIRED_FILES if file not in all_files]

            validation_status = not missing_files
            with open(self.config.STATUS_FILE, 'w') as f:
                f.write(f"Validation status: {validation_status}\n")
                if missing_files:
                    f.write(f"Missing files: {', '.join(missing_files)}\n")

            logger.info(f"Validation status: {validation_status}")
            if missing_files:
                logger.error(f"Missing files: {', '.join(missing_files)}")

            return validation_status

        except Exception as e:
            logger.error(f"Error during file validation: {e}")
            raise e
