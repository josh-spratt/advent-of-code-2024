from src.fetch_input_data import DataRetriever
from src.logger import AdventLogger
import os
import time

logger = AdventLogger("day11part01").get_logger()


def apply_ruleset(stone):
    if stone == 0:
        stone = 1
        return stone
    elif len(str(stone)) % 2 == 0:
        middle = len(str(stone)) // 2
        left_stone = int(str(stone)[:middle])
        right_stone = int(str(stone)[middle:])
        return left_stone, right_stone
    else:
        stone = stone * 2024
        return stone


def solve():
    start_time = time.time()
    logger.info("Starting to solve Day 11, Part 01")
    env = os.environ
    logger.debug("Fetching input data")
    data_retriever = DataRetriever(
        2024, 11, env["AOC_COOKIE"]
    )  # TODO: Don't forget to update the day if you copy/paste
    input_data_string = data_retriever.fetch_input_data().strip()
    
    all_new_stones = []

    stones = [int(stone) for stone in input_data_string.split(" ")]

    for i in range(25):
        new_stones = []
        for stone in stones:
            if len(str(stone)) % 2 == 0:
                left_stone, right_stone = apply_ruleset(stone)
                new_stones.append(left_stone)
                new_stones.append(right_stone)
            else:
                new_stone = apply_ruleset(stone)
                new_stones.append(new_stone)
        stones = new_stones

    logger.info(f"Number of stones: {len(stones)}")

    end_time = time.time()
    elapsed_time = end_time - start_time
    logger.info(f"Solution completed in {elapsed_time:.2f} seconds")
    return len(stones)
