from src.fetch_input_data import DataRetriever
from src.input_parser import parse_input_to_matrix
from src.logger import AdventLogger
import os
import time
from itertools import product

logger = AdventLogger("day07part02").get_logger()


def solve():
    start_time = time.time()
    logger.info("Starting to solve Day 07, Part 02")
    env = os.environ
    logger.debug("Fetching input data")
    data_retriever = DataRetriever(
        2024, 7, env["AOC_COOKIE"]
    )  # TODO: Don't forget to update the day if you copy/paste
    input_data_string = data_retriever.fetch_input_data()
    input_list = input_data_string.splitlines()

    counter = 0

    for item in input_list:
        key = int(item.split(": ")[0])
        numbers = [int(x) for x in item.split(": ")[1].split(" ")]
        
        for c in product("+*|", repeat=len(numbers) - 1):
            res = numbers[0]
            for i in range(1, len(numbers)):
                if c[i - 1] == "+":
                    res += numbers[i]
                elif c[i - 1] == "|":
                    res = int(str(res) + str(numbers[i]))
                else:
                    res *= numbers[i]
            if res == key:
                counter += key
                break
    logger.info(f"Total calibration result: {counter}")

    end_time = time.time()
    elapsed_time = end_time - start_time
    logger.info(f"Solution completed in {elapsed_time:.2f} seconds")
    return counter
