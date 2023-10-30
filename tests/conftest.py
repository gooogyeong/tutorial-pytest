import pytest

from source import shapes

# global fixture accessible in every file within tests/ directory
@pytest.fixture
def my_rectangle():
    return shapes.Rectangle(20, 10)


@pytest.fixture
def weird_rectangle():
    return shapes.Rectangle(6, 5)
