import pytest
from unittest.mock import patch
from solutions.day01.part_02 import solve

EXAMPLE_INPUT = """
3   4
4   3
2   5
1   3
3   9
3   3
"""


@patch("src.fetch_input_data.DataRetriever.fetch_input_data")
def test_solve(mock_fetch_data):
    mock_fetch_data.return_value = EXAMPLE_INPUT.strip()
    result = solve()
    assert result == 31
