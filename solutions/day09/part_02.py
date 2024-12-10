from src.fetch_input_data import DataRetriever
from src.input_parser import parse_input_to_list
from src.logger import AdventLogger
import os
import time
from collections import defaultdict

logger = AdventLogger("day09part02").get_logger()


def solve():
    start_time = time.time()
    logger.info("Starting to solve Day 09, Part 02")
    env = os.environ
    logger.debug("Fetching input data")
    data_retriever = DataRetriever(
        2024, 9, env["AOC_COOKIE"]
    )  # TODO: Don't forget to update the day if you copy/paste
    input_data_string = data_retriever.fetch_input_data().strip()

    id = 0
    position = 0

    file_map = {}
    empty_spots = []

    for i, char in enumerate(input_data_string):
        x = int(char)
        if i % 2 == 0:
            file_map[id] = (position, x)
            id += 1
        else:
            empty_spots.append((position, x))
        position += x

    while id > 0:
        id -= 1
        position, size = file_map[id]
        for i, (start, length) in enumerate(empty_spots):
            if start >= position:
                empty_spots = empty_spots[:i]
                break
            if size <= length:
                file_map[id] = (start, size)
                if size == length:
                    empty_spots.pop(i)
                else:
                    empty_spots[i] = (start + size, length - size)
                break

    total = 0

    for id, (position, size) in file_map.items():
        for x in range(position, position + size):
            total += id * x

    logger.info(f"Filesystem checksum: {total}")

    end_time = time.time()
    elapsed_time = end_time - start_time
    logger.info(f"Solution completed in {elapsed_time:.2f} seconds")
    return total
