#tests for the small calculator project

# import the calculator file
import calculator

# test the add function
def test_add():
    assert calculator.add(2, 3) == 5
    assert calculator.add(2,2) == 4

# test the subtract function
def test_subtract():
    assert calculator.subtract(2, 3) == -1
    assert calculator.subtract(2,2) == 0

# test the multiply function
def test_multiply():
    assert calculator.multiply(2, 3) == 6
    assert calculator.multiply(2,2) == 4

# test the divide function
def test_divide():
    assert calculator.divide(2, 3) == 0.6666666666666666
    assert calculator.divide(2,2) == 1

# Run the tests
# $ pytest test_calculator.py
# ============================= test session starts ==============================