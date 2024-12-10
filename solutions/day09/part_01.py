from src.fetch_input_data import DataRetriever
from src.input_parser import parse_input_to_list
from src.logger import AdventLogger
import os
import time
from collections import defaultdict

logger = AdventLogger("day09part01").get_logger()


def solve():
    start_time = time.time()
    logger.info("Starting to solve Day 09, Part 01")
    env = os.environ
    logger.debug("Fetching input data")
    data_retriever = DataRetriever(
        2024, 9, env["AOC_COOKIE"]
    )  # TODO: Don't forget to update the day if you copy/paste
    input_data_string = data_retriever.fetch_input_data().strip()

    transformed_input = []

    id = 0

    for i, char in enumerate(input_data_string):
        if i % 2 != 0:
            for j in range(int(char)):
                transformed_input.append(".")
        else:
            id += 1
            for _ in range(int(char)):
                transformed_input.append(str(id - 1))

    empty_spots = [i for i, n in enumerate(transformed_input) if n == "."]

    total = 0

    for spot in empty_spots:
        while transformed_input[-1] == ".":
            transformed_input.pop()
        if len(transformed_input) <= spot:
            break
        transformed_input[spot] = transformed_input.pop()
    
    for i, n in enumerate(transformed_input):
        total += (int(n) * i)

    logger.info(f"Filesystem checksum: {total}")

    end_time = time.time()
    elapsed_time = end_time - start_time
    logger.info(f"Solution completed in {elapsed_time:.2f} seconds")
    return total
