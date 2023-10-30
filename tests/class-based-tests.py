import source.shapes as shapes
import math


# Test- prefix in class name -> auto-discovery of tests
class TestCircle:
    def setup_method(self, method):
        print(f"Setting up {method}")
        self.circle = shapes.Circle(10)

    def teardown_method(self, method):
        print(f"Tearing down {method}")
        del self.circle

    def test_area(self):
        print("test-    area ===")
        assert self.circle.area() == math.pi * (self.circle.radius**2)

    def test_perimeter(self):
        assert self.circle.perimeter() == 2 * math.pi * self.circle.radius

# poetry run pytest -s tests/class-based-tests.py

# ================== test session starts ==================
# platform darwin -- Python 3.9.2, pytest-7.4.3, pluggy-1.3.0
# rootdir: /Users/minkyunglee/Desktop/code/tutorial-pytest
# collected 2 items                                       

# tests/class-based-tests.py Setting up <bound method TestCircle.test_area of <tests.class-based-tests.TestCircle object at 0x101cb4070>>
# test-    area ===
# .Tearing down <bound method TestCircle.test_area of <tests.class-based-tests.TestCircle object at 0x101cb4070>>
# Setting up <bound method TestCircle.test_perimeter of <tests.class-based-tests.TestCircle object at 0x101cb4190>>
# .Tearing down <bound method TestCircle.test_perimeter of <tests.class-based-tests.TestCircle object at 0x101cb4190>>


# =================== 2 passed in 0.00s ===================