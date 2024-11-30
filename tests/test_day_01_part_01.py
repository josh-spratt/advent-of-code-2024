import pytest
from unittest.mock import patch
from solutions.day_01_part_01 import solve

EXAMPLE_INPUT = """
1abc2
pqr3stu8vwx
a1b2c3d4e5f
treb7uchet
"""


@patch("src.fetch_input_data.DataRetriever.fetch_input_data")
def test_solve(mock_fetch_data):
    mock_fetch_data.return_value = EXAMPLE_INPUT.strip()
    result = solve()
    assert result == 142
