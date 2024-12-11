from src.fetch_input_data import (
    DataRetriever,
)
from src.input_parser import (
    parse_input_to_matrix,
)
from src.logger import AdventLogger
import os
import time

logger = AdventLogger("day10part01").get_logger()


def dfs(topographic_map, x, y, visited, movements):
    """
    Perform Depth-First Search (DFS) to find all reachable '9's in the topographic map starting from (x, y).

    Args:
        topographic_map (list of lists): 2D matrix representing the map with heights.
        x (int): Current row index in the map.
        y (int): Current column index in the map.
        visited (set): Set of visited coordinates to avoid revisiting.
        movements (list of tuples): Allowed movement directions as (dx, dy).

    Returns:
        set: A set of coordinates where '9' is reachable from (x, y).
    """
    rows = len(topographic_map)  # Number of rows in the map
    columns = len(topographic_map[0])  # Number of columns in the map

    # If the current coordinate has already been visited, terminate this path
    if (x, y) in visited:
        return set()

    # Mark the current coordinate as visited
    visited.add((x, y))

    # If the current position is a '9', return it as a single-element set
    if topographic_map[x][y] == 9:
        return {(x, y)}

    # Initialize a set to collect reachable '9's
    reachable_nines = set()

    # Explore all possible movement directions
    for dx, dy in movements:
        nx, ny = x + dx, y + dy  # Calculate new coordinates after moving
        # Check if the new coordinates are within bounds of the map
        if 0 <= nx < rows and 0 <= ny < columns:
            # Proceed only if the next cell's value is exactly one greater than the current cell
            if topographic_map[nx][ny] == topographic_map[x][y] + 1:
                # Recursively call DFS and union the results
                reachable_nines |= dfs(topographic_map, nx, ny, visited, movements)

    return reachable_nines


def count_nines_from_trailheads(topographic_map, trailheads, movements):
    """
    Count the number of unique '9's reachable from each trailhead.

    Args:
        topographic_map (list of lists): 2D matrix of the map with heights.
        trailheads (list of tuples): List of coordinates to start the search.
        movements (list of tuples): Allowed movement directions as (dx, dy).

    Returns:
        list: A list of counts of unique '9's reachable from each trailhead.
    """
    results = []  # List to store the counts for each trailhead
    for trailhead in trailheads:
        visited = set()  # Reset visited set for each trailhead
        # Use DFS to find all '9's reachable from the current trailhead
        nines_reached = dfs(
            topographic_map, trailhead[0], trailhead[1], visited, movements
        )
        # Append the count of reachable '9's to the results
        results.append(len(nines_reached))
    return results


def solve():
    """
    Main function to solve Day 10, Part 01 of the Advent of Code challenge.

    Returns:
        int: Sum of all unique '9's reachable from trailheads.
    """
    # Start timing the solution
    start_time = time.time()
    logger.info("Starting to solve Day 10, Part 01")

    # Fetch input data from the environment variable and parse it
    env = os.environ
    logger.debug("Fetching input data")
    data_retriever = DataRetriever(
        2024, 10, env["AOC_COOKIE"]
    )  # TODO: Update the day if reusing this script
    input_data_string = (
        data_retriever.fetch_input_data().strip()
    )  # Fetch and clean input data

    # Parse the input into a 2D list (matrix) of integers
    topographic_map = [
        [int(x) for x in y] for y in parse_input_to_matrix(input_data_string)
    ]

    rows = len(topographic_map)  # Number of rows in the map
    columns = len(topographic_map[0])  # Number of columns in the map

    # Define possible movements: right, down, left, up
    movements = [(0, 1), (1, 0), (0, -1), (-1, 0)]

    # Identify all trailhead positions where the value is '0'
    trailheads = []
    for i in range(rows):
        for j in range(columns):
            if topographic_map[i][j] == 0:
                trailheads.append((i, j))

    # Count all unique '9's reachable from each trailhead
    result = count_nines_from_trailheads(topographic_map, trailheads, movements)

    # Print and return the sum of all results
    logger.info(f"Trailhead scores: {sum(result)}")

    # End timing the solution
    end_time = time.time()
    elapsed_time = end_time - start_time
    logger.info(f"Solution completed in {elapsed_time:.2f} seconds")
    return sum(result)
