import pytest
from unittest.mock import patch
from solutions.day12.part_02 import solve

EXAMPLE_INPUT = """
"""


@patch("src.fetch_input_data.DataRetriever.fetch_input_data")
def test_solve(mock_fetch_data):
    mock_fetch_data.return_value = EXAMPLE_INPUT.strip()
    result = solve()
    assert result == None
