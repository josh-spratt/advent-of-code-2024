import pytest
from unittest.mock import patch
from solutions.day09.part_02 import solve

EXAMPLE_INPUT = """
2333133121414131402
"""


@patch("src.fetch_input_data.DataRetriever.fetch_input_data")
def test_solve(mock_fetch_data):
    mock_fetch_data.return_value = EXAMPLE_INPUT.strip()
    result = solve()
    assert result == 2858
