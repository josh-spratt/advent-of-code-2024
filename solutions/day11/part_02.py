from src.fetch_input_data import DataRetriever
from src.logger import AdventLogger
import os
import time
from functools import cache

logger = AdventLogger("day11part02").get_logger()


@cache
def apply_ruleset(stone, iterations):
    if iterations == 0:
        return 1
    if stone == 0:
        return apply_ruleset(1, iterations - 1)
    elif len(str(stone)) % 2 == 0:
        middle = len(str(stone)) // 2
        left_stone = int(str(stone)[:middle])
        right_stone = int(str(stone)[middle:])
        return apply_ruleset(left_stone, iterations - 1) + apply_ruleset(right_stone, iterations - 1)
    else:
        return apply_ruleset(stone * 2024, iterations - 1)


def solve():
    start_time = time.time()
    logger.info("Starting to solve Day 11, Part 02")
    env = os.environ
    logger.debug("Fetching input data")
    data_retriever = DataRetriever(
        2024, 11, env["AOC_COOKIE"]
    )  # TODO: Don't forget to update the day if you copy/paste
    input_data_string = data_retriever.fetch_input_data().strip()
    
    all_new_stones = []

    stones = [int(stone) for stone in input_data_string.split(" ")]

    counter = 0
    for stone in stones:
        stone_count = apply_ruleset(stone, 75)
        counter += stone_count
    
    logger.info(f"Number of stones: {counter}")

    end_time = time.time()
    elapsed_time = end_time - start_time
    logger.info(f"Solution completed in {elapsed_time:.2f} seconds")
    return counter
