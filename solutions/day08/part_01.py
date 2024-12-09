from src.fetch_input_data import DataRetriever
from src.input_parser import parse_input_to_matrix
from src.logger import AdventLogger
import os
import time
from collections import defaultdict

logger = AdventLogger("day08part01").get_logger()


def solve():
    start_time = time.time()
    logger.info("Starting to solve Day 08, Part 01")
    env = os.environ
    logger.debug("Fetching input data")
    data_retriever = DataRetriever(
        2024, 8, env["AOC_COOKIE"]
    )  # TODO: Don't forget to update the day if you copy/paste
    input_data_string = data_retriever.fetch_input_data()
    input_matrix = parse_input_to_matrix(input_data_string)
    
    rows = len(input_matrix)
    columns = len(input_matrix[0])

    antenna_map = {}

    for r, row in enumerate(input_matrix):
        for c, char in enumerate(row):
            if char != ".":
                if char not in antenna_map:
                    antenna_map[char] = []
                antenna_map[char].append((r, c))
    
    antinodes = set()

    for coords in antenna_map.values():
        for i in range(len(coords)):
            for j in range(i + 1, len(coords)):
                r1, c1 = coords[i]
                r2, c2 = coords[j]
                antinodes.add((2 * r1 - r2, 2 * c1 - c2))
                antinodes.add((2 * r2 - r1, 2 * c2 - c1))
    
    counter = 0
    for antinode in antinodes:
        if (antinode[0] >= 0 and antinode[0] <= rows - 1) and (antinode[1] >= 0 and antinode[1] <= columns - 1):
            counter += 1
    
    logger.info(f"Number of antinodes: {counter}")

    end_time = time.time()
    elapsed_time = end_time - start_time
    logger.info(f"Solution completed in {elapsed_time:.2f} seconds")
    return counter
