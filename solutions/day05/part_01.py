from src.fetch_input_data import DataRetriever
from src.input_parser import parse_input_to_matrix
from src.logger import AdventLogger
import os
import time

logger = AdventLogger("day05part01").get_logger()


def solve():
    start_time = time.time()
    logger.info("Starting to solve Day 05, Part 01")
    env = os.environ
    logger.debug("Fetching input data")
    data_retriever = DataRetriever(2024, 1, env["AOC_COOKIE"])
    input_data_string = data_retriever.fetch_input_data()

    end_time = time.time()
    elapsed_time = end_time - start_time
    logger.info(f"Solution completed in {elapsed_time:.2f} seconds")
    return None
