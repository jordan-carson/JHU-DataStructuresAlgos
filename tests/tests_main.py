import pytest
# from unittest import mock

from core.main import converter


@pytest.mark.parametrize("input, result", [
    ("*AB", "AB*"),

])
def test_converter_part1(input, result):
    assert converter(input) == result
