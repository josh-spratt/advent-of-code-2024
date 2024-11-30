import logging
from logging import Logger

class AdventLogger:
    def __init__(self, name: str, level: int = logging.INFO):
        self.logger = logging.getLogger(name)
        self.logger.setLevel(level)

        console_handler = logging.StreamHandler()
        console_handler.setLevel(level)

        formatter = logging.Formatter(fmt="%(asctime)s - %(name)s - %(levelname)s - %(message)s", datefmt="%Y-%m-%d %H:%M:%S")

        console_handler.setFormatter(formatter)

        if not self.logger.hasHandlers():
            self.logger.addHandler(console_handler)
    
    def get_logger(self) -> Logger:
        return self.logger
