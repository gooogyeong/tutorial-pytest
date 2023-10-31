import pytest
import source.my_functions as my_functions

# function-based tests

# pytest by default doesn't look for tests in files not named like test_*.py


# test_ prefix -> auto-discovery of tests
# 이렇게 안하면 test로 인식 X
# =============================== no tests ran in 0.00s ===============================
def test_add():
    # pass
    result = my_functions.add(1, 4)
    assert my_functions.add(1, 4) == 5
    # assert my_functions.add(1, 4) == 6  # AssertionError


def test_add_strings():
    result = my_functions.add("Hello", " World")
    assert result == "Hello World"


def test_divide():
    result = my_functions.divide(10, 2)
    assert result == 5


def test_divide_by_zero():
    # result = my_functions.divide(10, 0) # ZeroDivisionError: division by zero

    # with pytest.raises(ValueError):
    #     result = my_functions.divide(10, 0)

    with pytest.raises(ZeroDivisionError):
        result = my_functions.divide(10, 0)
