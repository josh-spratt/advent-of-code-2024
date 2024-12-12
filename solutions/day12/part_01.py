from src.fetch_input_data import DataRetriever
from src.logger import AdventLogger
import os
import time

logger = AdventLogger("day12part01").get_logger()


def solve():
    start_time = time.time()
    logger.info("Starting to solve Day 12, Part 01")
    env = os.environ
    logger.debug("Fetching input data")
    data_retriever = DataRetriever(
        2024, 12, env["AOC_COOKIE"]
    )  # TODO: Don't forget to update the day if you copy/paste
    input_data_string = data_retriever.fetch_input_data().strip()

    end_time = time.time()
    elapsed_time = end_time - start_time
    logger.info(f"Solution completed in {elapsed_time:.2f} seconds")
    return None
