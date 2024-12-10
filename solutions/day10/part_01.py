from src.fetch_input_data import DataRetriever
from src.input_parser import parse_input_to_list
from src.logger import AdventLogger
import os
import time
from collections import defaultdict

logger = AdventLogger("day10part01").get_logger()


def solve():
    start_time = time.time()
    logger.info("Starting to solve Day 10, Part 01")
    env = os.environ
    logger.debug("Fetching input data")
    data_retriever = DataRetriever(
        2024, 10, env["AOC_COOKIE"]
    )  # TODO: Don't forget to update the day if you copy/paste
    input_data_string = data_retriever.fetch_input_data().strip()

    end_time = time.time()
    elapsed_time = end_time - start_time
    logger.info(f"Solution completed in {elapsed_time:.2f} seconds")
    return None
