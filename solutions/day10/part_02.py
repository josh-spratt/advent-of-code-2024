from src.fetch_input_data import (
    DataRetriever,
)
from src.input_parser import (
    parse_input_to_matrix,
)
from src.logger import AdventLogger
import os
import time

logger = AdventLogger("day10part02").get_logger()


def dfs(topographic_map, x, y, visited, movements, current_path):
    """
    Perform Depth-First Search (DFS) to find all paths to '9's from a given starting point.

    Args:
        topographic_map (list of lists): 2D matrix representing the map with heights.
        x (int): Current row index in the map.
        y (int): Current column index in the map.
        visited (set): Set of visited coordinates to avoid revisiting.
        movements (list of tuples): Allowed movement directions as (dx, dy).
        current_path (list of tuples): List storing the current path during DFS.

    Returns:
        dict: A dictionary where keys are coordinates of '9's and values are lists of paths to each '9'.
    """
    rows = len(topographic_map)  # Number of rows in the map
    columns = len(topographic_map[0])  # Number of columns in the map

    # If the current coordinate has already been visited, terminate this path
    if (x, y) in visited:
        return {}

    # Mark the current coordinate as visited and add it to the current path
    visited.add((x, y))
    current_path.append((x, y))

    # Dictionary to store paths to reachable '9's
    paths_to_nines = {}

    # If the current position is a '9', store the current path
    if topographic_map[x][y] == 9:
        paths_to_nines[(x, y)] = [list(current_path)]  # Copy the path to avoid mutation
    else:
        # Explore all possible movement directions
        for dx, dy in movements:
            nx, ny = x + dx, y + dy  # Calculate new coordinates after moving
            # Check if the new coordinates are within bounds of the map
            if 0 <= nx < rows and 0 <= ny < columns:
                # Proceed only if the next cell's value is exactly one greater than the current cell
                if topographic_map[nx][ny] == topographic_map[x][y] + 1:
                    # Recursively collect paths from neighbors
                    neighbor_paths = dfs(
                        topographic_map, nx, ny, visited, movements, current_path
                    )
                    # Merge paths from neighbors into the current paths dictionary
                    for nine, paths in neighbor_paths.items():
                        if nine not in paths_to_nines:
                            paths_to_nines[nine] = []
                        paths_to_nines[nine].extend(paths)

    # Backtrack: remove the current coordinate from the path and unmark it as visited
    current_path.pop()
    visited.remove((x, y))

    return paths_to_nines


def find_paths_to_nines(topographic_map, trailheads, movements):
    """
    Find all paths to '9's from each trailhead.

    Args:
        topographic_map (list of lists): 2D matrix of the map with heights.
        trailheads (list of tuples): List of coordinates to start the search.
        movements (list of tuples): Allowed movement directions as (dx, dy).

    Returns:
        dict: A dictionary where keys are trailheads and values are dictionaries of paths to '9's.
    """
    all_paths = {}  # Dictionary to store paths for all trailheads
    for trailhead in trailheads:
        visited = set()  # Reset visited set for each trailhead
        # Use DFS to find paths to all '9's from the current trailhead
        paths = dfs(topographic_map, trailhead[0], trailhead[1], visited, movements, [])
        all_paths[trailhead] = paths  # Store the paths in the result dictionary
    return all_paths


def solve():
    """
    Main function to solve Day 10, Part 02 of the Advent of Code challenge.

    Returns:
        int: Total count of unique paths to '9's across all trailheads.
    """
    # Start timing the solution
    start_time = time.time()
    logger.info("Starting to solve Day 10, Part 02")

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

    # Find all paths to '9's from the trailheads
    all_paths = find_paths_to_nines(topographic_map, trailheads, movements)

    # Initialize a counter for the total number of paths
    scores = 0
    for trailhead, paths in all_paths.items():
        for nine, path_list in paths.items():
            # Log each '9' and its corresponding paths for debugging or review
            scores += len(
                path_list
            )  # Increment the total count by the number of paths to this '9'

    # Print the total score for debugging or output
    logger.info(f"Trailhead scores: {scores}")

    # End timing the solution
    end_time = time.time()
    elapsed_time = end_time - start_time
    logger.info(f"Solution completed in {elapsed_time:.2f} seconds")
    return scores
