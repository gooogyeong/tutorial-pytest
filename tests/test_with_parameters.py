import pytest

import source.shapes as shapes


@pytest.mark.parametrize("side, expected_area", [(2, 4), (3, 9), (10, 100)])
def test_multiple_square_areas(side, expected_area):
    square = shapes.Square(side)
    assert square.area() == expected_area

@pytest.mark.parametrize("side, expected_perimeter", [(3, 12), (4, 16), (5, 20), (10, 40)])
def test_multiple_square_perimeters(side, expected_perimeter):
    square = shapes.Square(side)
    assert square.perimeter() == expected_perimeter