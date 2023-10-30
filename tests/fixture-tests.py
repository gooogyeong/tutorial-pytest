import pytest
import source.shapes as shapes

# local fixture
# @pytest.fixture
# def my_rectangle():
#     return shapes.Rectangle(20, 10)

# @pytest.fixture
# def weird_rectangle():
#     return shapes.Rectangle(6, 5)


def test_area(my_rectangle):
    # my_rectangle = shapes.Rectangle(20, 10)
    assert my_rectangle.area() == 200


def test_perimeter(my_rectangle):
    # my_rectangle = shapes.Rectangle(20, 10)
    assert my_rectangle.perimeter() == 60

def test_eq(my_rectangle, weird_rectangle):
    assert my_rectangle != weird_rectangle