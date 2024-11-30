from src.fetch_input_data import DataRetriever
from src.input_parser import parse_input_to_list
from src.logger import AdventLogger
import os
import time

logger = AdventLogger("day01part01").get_logger()


def solve():
    start_time = time.time()
    logger.info("Starting to solve Day 01, Part 01")
    env = os.environ
    logger.debug("Fetching input data")
    data_retriever = DataRetriever(2023, 1, env["AOC_COOKIE"])
    input_data_string = data_retriever.fetch_input_data()
    logger.debug("Parsing input data to a list")
    input_list = parse_input_to_list(input_data_string)

    numbers = []

    logger.debug("Processing input data")
    for line in input_list:
        number = ""
        for char in line:
            if char.isdigit():
                number += char
                break
        for char in line[::-1]:
            if char.isdigit():
                number += char
                break
        numbers.append(int(number))
    logger.info(f"Sum of all calibration values: {sum(numbers)}")
    end_time = time.time()
    elapsed_time = end_time - start_time
    logger.info(f"Solution completed in {elapsed_time:.2f} seconds")
    return sum(numbers)
