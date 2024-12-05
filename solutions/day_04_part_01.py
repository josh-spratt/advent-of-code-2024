from src.fetch_input_data import DataRetriever
from src.input_parser import parse_input_to_matrix
from src.logger import AdventLogger
import os
import time

logger = AdventLogger("day04part01").get_logger()


def get_next_characters(matrix):
    rows, cols = len(matrix), len(matrix[0])
    directions = [
        (0, 1),  # right
        (0, -1),  # left
        (1, 0),  # down
        (-1, 0),  # up
        (1, 1),  # diagonal down-right
        (-1, -1),  # diagonal up-left
        (1, -1),  # diagonal down-left
        (-1, 1),  # diagonal up-right
    ]

    def get_next_chars_in_direction(x, y, dx, dy):
        """Get next three characters in the given direction (dx, dy), checking bounds"""
        chars = []
        for i in range(1, 4):  # Only next 3 characters
            nx, ny = x + i * dx, y + i * dy
            if 0 <= nx < rows and 0 <= ny < cols:
                chars.append(matrix[nx][ny])
            else:
                chars.append(None)  # If out of bounds, append None
        return chars

    result = {}
    for r in range(rows):
        for c in range(cols):
            if matrix[r][c] == "X":
                result[(r, c)] = {}

                # For each direction, collect the next 3 characters
                for dx, dy in directions:
                    direction_name = f"direction_{dx}_{dy}"
                    result[(r, c)][direction_name] = get_next_chars_in_direction(
                        r, c, dx, dy
                    )

    return result


def count_specific_sequence(result, target_sequence):
    count = 0
    for position, directions in result.items():
        for direction, chars in directions.items():
            if chars == target_sequence:
                count += 1
    return count


def solve():
    start_time = time.time()
    logger.info("Starting to solve Day 04, Part 01")
    env = os.environ
    logger.debug("Fetching input data")
    data_retriever = DataRetriever(2024, 4, env["AOC_COOKIE"])
    input_data_string = data_retriever.fetch_input_data()
    input_matrix = parse_input_to_matrix(input_data_string)

    result = get_next_characters(input_matrix)
    final_result = count_specific_sequence(result, ["M", "A", "S"])

    logger.info(f"XMAS word search count: {final_result}")

    end_time = time.time()
    elapsed_time = end_time - start_time
    logger.info(f"Solution completed in {elapsed_time:.2f} seconds")
    return final_result
