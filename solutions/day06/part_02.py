from src.fetch_input_data import DataRetriever
from src.input_parser import parse_input_to_matrix
from src.logger import AdventLogger
import os
import time

logger = AdventLogger("day06part02").get_logger()


direction_map = {"up": (-1, 0), "right": (0, 1), "down": (1, 0), "left": (0, -1)}

directions = ["up", "right", "down", "left"]


def check_for_infinite_loop(matrix, start_x, start_y, start_facing):
    visited = set()  # To track visited positions and directions
    x, y, facing = start_x, start_y, start_facing

    while True:
        # If we've already visited this position with the same facing direction, it's a loop
        if (x, y, facing) in visited:
            return True  # Infinite loop detected

        visited.add((x, y, facing))

        dx, dy = direction_map[facing]
        nx, ny = x + dx, y + dy

        # Check if the next move is outside the grid (exit condition)
        if not (0 <= nx < len(matrix) and 0 <= ny < len(matrix[0])):
            return False  # Exit condition, no infinite loop

        # Check if the next position is valid (inside grid and not blocked)
        if matrix[nx][ny] != "#":
            x, y = nx, ny  # Move to the next position
        else:
            # Turn right if blocked
            current_index = directions.index(facing)
            facing = directions[(current_index + 1) % len(directions)]


def solve():
    start_time = time.time()
    logger.info("Starting to solve Day 06, Part 02")
    env = os.environ
    logger.debug("Fetching input data")
    data_retriever = DataRetriever(
        2024, 6, env["AOC_COOKIE"]
    )  # TODO: Don't forget to update the day if you copy/paste
    input_data_string = data_retriever.fetch_input_data()
    matrix = parse_input_to_matrix(input_data_string)

    facing = "up"

    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            if matrix[i][j] == "^":
                x, y = i, j
                break

    count = 0
    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            # Simulate placing a blocker at (i, j)
            if matrix[i][j] != "#":
                matrix[i][j] = "#"  # Temporarily block this position

                # Check if placing the blocker causes an infinite loop
                if check_for_infinite_loop(matrix, x, y, facing):
                    count += 1

                matrix[i][j] = "."  # Reset the position

    logger.info(f"Infinite loop positions: {count}")

    end_time = time.time()
    elapsed_time = end_time - start_time
    logger.info(f"Solution completed in {elapsed_time:.2f} seconds")
    return count
