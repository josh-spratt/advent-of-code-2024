from src.fetch_input_data import DataRetriever
from src.input_parser import parse_input_to_matrix
from src.logger import AdventLogger
import os
import time

logger = AdventLogger("day01part01").get_logger()


def solve():
    start_time = time.time()
    logger.info("Starting to solve Day 01, Part 01")
    env = os.environ
    logger.debug("Fetching input data")
    data_retriever = DataRetriever(2024, 1, env["AOC_COOKIE"])
    input_data_string = data_retriever.fetch_input_data()
    matrix = parse_input_to_matrix(input_data=input_data_string, delimeter="   ")

    left_locations_list = [int(x[0]) for x in matrix]
    right_locations_list = [int(x[1]) for x in matrix]
    left_locations_list.sort()
    right_locations_list.sort()

    total_distance = 0
    for i in range(len(left_locations_list)):
        total_distance += abs(left_locations_list[i] - right_locations_list[i])

    logger.info(f"The total distance is: {total_distance}")

    end_time = time.time()
    elapsed_time = end_time - start_time
    logger.info(f"Solution completed in {elapsed_time:.2f} seconds")
    return total_distance
