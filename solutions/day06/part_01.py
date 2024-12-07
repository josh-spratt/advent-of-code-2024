from src.fetch_input_data import DataRetriever
from src.input_parser import parse_input_to_matrix
from src.logger import AdventLogger
import os
import time

logger = AdventLogger("day06part01").get_logger()


def solve():
    start_time = time.time()
    logger.info("Starting to solve Day 06, Part 01")
    env = os.environ
    logger.debug("Fetching input data")
    data_retriever = DataRetriever(
        2024, 6, env["AOC_COOKIE"]
    )  # TODO: Don't forget to update the day if you copy/paste
    input_data_string = data_retriever.fetch_input_data()
    matrix = parse_input_to_matrix(input_data_string)
    
    direction_map = {
        "up": (-1, 0),
        "right": (0, 1),
        "down": (1, 0),
        "left": (0, -1)
    }

    directions = ["up", "right", "down", "left"]
    facing = "up"

    # identify starting position
    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            if matrix[i][j] == "^":
                x, y = i, j
                break
    
    visited_positions = set()

    while True:
        dx, dy = direction_map[facing]
        nx, ny = x + dx, y + dy

        if not (0 <= nx < len(matrix) and 0 <= ny < len(matrix[0])):
            logger.info(f"Character exited the grid at ({x}, {y}) facing {facing}")
            break

        if 0 <= nx < len(matrix) and 0 <= ny < len(matrix[0]) and matrix[nx][ny] != "#":
            x, y = nx, ny
            matrix[x][y] = "x"
            visited_positions.add((x, y))
        else:
            current_index = directions.index(facing)
            facing = directions[(current_index + 1) % len(directions)]

    logger.info(f"Distinct positions visited: {len(visited_positions) + 1}")

    end_time = time.time()
    elapsed_time = end_time - start_time
    logger.info(f"Solution completed in {elapsed_time:.2f} seconds")
    return len(visited_positions) + 1  # LOL, too tired to worry about this...
