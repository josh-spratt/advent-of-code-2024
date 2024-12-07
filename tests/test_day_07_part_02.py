import pytest
from unittest.mock import patch
from solutions.day07.part_02 import solve

EXAMPLE_INPUT = """
190: 10 19
3267: 81 40 27
83: 17 5
156: 15 6
7290: 6 8 6 15
161011: 16 10 13
192: 17 8 14
21037: 9 7 18 13
292: 11 6 16 20
"""


@patch("src.fetch_input_data.DataRetriever.fetch_input_data")
def test_solve(mock_fetch_data):
    mock_fetch_data.return_value = EXAMPLE_INPUT.strip()
    result = solve()
    assert result == 11387
