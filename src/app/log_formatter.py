import json
import logging


class JSONFormatter(logging.Formatter):
    def format(self, record):
        log_record = {
            "level": record.levelname,
            "message": record.getMessage(),
            "timestamp": self.formatTime(record, self.datefmt),
            "function": record.funcName,
            "module": record.module,
        }

        if hasattr(record, 'inputs'):
            log_record['inputs'] = record.inputs

        return json.dumps(log_record)


