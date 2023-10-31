import pytest
import source.my_functions as my_functions
import time

@pytest.mark.slow  # telling pytest that this is slow
def test_slow():
    time.sleep(5)
    result = my_functions.divide(10, 2)
    assert result == 5

# poetry run pytest -m [MARKER_NAME]
# poetry run pytest tests/ -m slow # only runs test with @pytest.mark.slow decorator

# ================== test session starts ===================
# platform darwin -- Python 3.9.2, pytest-7.4.3, pluggy-1.3.0
# rootdir: /Users/minkyunglee/Desktop/code/tutorial-pytest/tests
# configfile: pytest.ini
# collected 11 items / 10 deselected / 1 selected          

# tests/test_function_style.py .                     [100%]

# ============ 1 passed, 10 deselected in 5.02s ============

# skips test
@pytest.mark.skip(reason="This feature is currently broken")
def test_add():
    assert my_functions.add(1, 2) == 3

# marks the test function as an expected failure
@pytest.mark.xfail
def test_divide_by_zero(reason="No number can be divided by zero"):
  my_functions.divide(10, 0)
