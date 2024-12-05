from src.fetch_input_data import DataRetriever
from src.logger import AdventLogger
import os
import time
import re

logger = AdventLogger("day03part02").get_logger()


def solve():
    start_time = time.time()
    logger.info("Starting to solve Day 03, Part 02")
    env = os.environ
    logger.debug("Fetching input data")
    data_retriever = DataRetriever(2024, 3, env["AOC_COOKIE"])
    input_data_string = data_retriever.fetch_input_data()

    mul_pattern = re.compile(r"mul\((\d+),(\d+)\)")

    chunks = re.split(r"(don't\(\)|do\(\))", input_data_string)

    result = []
    include = True

    for x in chunks:
        if x == "don't()":
            include = False
        elif x == "do()":
            include = True
        elif include:
            matches = mul_pattern.findall(x)
            result.extend([[int(num1), int(num2)] for num1, num2 in matches])

    result_sum = sum([x[0] * x[1] for x in result])
    logger.info(f"Uncorrupted mul instructions: {result_sum}")

    end_time = time.time()
    elapsed_time = end_time - start_time
    logger.info(f"Solution completed in {elapsed_time:.2f} seconds")
    return result_sum
