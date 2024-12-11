import pytest
from unittest.mock import patch
from solutions.day10.part_01 import solve

EXAMPLE_INPUT = """
89010123
78121874
87430965
96549874
45678903
32019012
01329801
10456732
"""


@patch("src.fetch_input_data.DataRetriever.fetch_input_data")
def test_solve(mock_fetch_data):
    mock_fetch_data.return_value = EXAMPLE_INPUT.strip()
    result = solve()
    assert result == 36
