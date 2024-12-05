from src.fetch_input_data import DataRetriever
from src.input_parser import parse_input_to_matrix
from src.logger import AdventLogger
import os
import time
from collections import Counter
import json

logger = AdventLogger("day04part02").get_logger()


def get_diagonals(matrix, r, c):
    """Return the diagonals for the 'A' character at position (r, c)."""
    rows, cols = len(matrix), len(matrix[0])

    # Ensure we're within bounds to check diagonals
    if r - 1 < 0 or r + 1 >= rows or c - 1 < 0 or c + 1 >= cols:
        return [], []  # Return empty lists if out of bounds

    # Top-left to bottom-right diagonal (M.A.S)
    diag_tl_br = [matrix[r - 1][c - 1], matrix[r][c], matrix[r + 1][c + 1]]

    # Top-right to bottom-left diagonal (S.A.M)
    diag_tr_bl = [matrix[r - 1][c + 1], matrix[r][c], matrix[r + 1][c - 1]]

    return diag_tl_br, diag_tr_bl


def count_x_shapes(matrix):
    """Count how many 'A' characters form an X shape with 'M' and 'S'."""
    count = 0
    rows, cols = len(matrix), len(matrix[0])

    for r in range(1, rows - 1):  # Start from 1 to avoid index out of bounds
        for c in range(1, cols - 1):  # Start from 1 to avoid index out of bounds
            if matrix[r][c] == "A":
                diag_tl_br, diag_tr_bl = get_diagonals(matrix, r, c)

                # Check if either diagonal matches ['M', 'A', 'S'] or ['S', 'A', 'M']
                if (
                    diag_tl_br == ["M", "A", "S"] or diag_tl_br == ["S", "A", "M"]
                ) and (diag_tr_bl == ["M", "A", "S"] or diag_tr_bl == ["S", "A", "M"]):
                    count += 1
    return count


def solve():
    start_time = time.time()
    logger.info("Starting to solve Day 04, Part 02")
    env = os.environ
    logger.debug("Fetching input data")
    data_retriever = DataRetriever(2024, 4, env["AOC_COOKIE"])
    input_data_string = data_retriever.fetch_input_data()
    input_matrix = parse_input_to_matrix(input_data_string)

    result = count_x_shapes(input_matrix)
    logger.info(f"XMAS word search count: {result}")

    end_time = time.time()
    elapsed_time = end_time - start_time
    logger.info(f"Solution completed in {elapsed_time:.2f} seconds")
    return result
