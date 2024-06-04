import os
import logging
from app.log_formatter import JSONFormatter


DEBUG = os.getenv('DEBUG', 'False').lower() == 'true'

logger = logging.getLogger()
logger.setLevel("ERROR")

for handler in logger.handlers:
    handler.setFormatter(JSONFormatter())
