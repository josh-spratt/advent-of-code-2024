from src.fetch_input_data import DataRetriever
from src.input_parser import parse_input_to_matrix
from src.logger import AdventLogger
import os
import time

logger = AdventLogger("day01part02").get_logger()


def solve():
    start_time = time.time()
    logger.info("Starting to solve Day 01, Part 02")
    env = os.environ
    logger.debug("Fetching input data")
    data_retriever = DataRetriever(2024, 1, env["AOC_COOKIE"])
    input_data_string = data_retriever.fetch_input_data()
    matrix = parse_input_to_matrix(input_data=input_data_string, delimeter="   ")

    left_locations_list = [int(x[0]) for x in matrix]
    right_locations_list = [int(x[1]) for x in matrix]
    right_locations_list_hist = {k: right_locations_list.count(k) for k in set(right_locations_list)}
    left_locations_list.sort()

    similarity_score = 0
    for i in range(len(left_locations_list)):
        try:
            similarity_score += left_locations_list[i] * right_locations_list_hist[left_locations_list[i]]
        except KeyError:
            logger.debug("Item does not exist in right list")

    logger.info(f"The similarity score is: {similarity_score}")

    end_time = time.time()
    elapsed_time = end_time - start_time
    logger.info(f"Solution completed in {elapsed_time:.2f} seconds")
    return similarity_score
