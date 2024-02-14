import math

def area(r):
    area = math.pi * pow(r, 2)
    return area

def test_area_function():
    # Test the area calculation with positive radius
    assert area(1) == math.pi
    assert area(2) == 4 * math.pi
    assert area(3) == 9 * math.pi

    # Test the area calculation with zero radius
    assert area(0) == 0

    # Test the area calculation with negative radius
    try:
        area(-1)
        print("Test failed: No exception raised for negative radius.")
    except ValueError:
        print("Test passed: Exception raised for negative radius.")


def test_area_function1():
    # Test the area calculation with positive radius
    assert area(1) == math.pi
    assert area(2) == 4 * math.pi
    assert area(0) == 9 * math.pi

    # Test the area calculation with zero radius
    assert area(0) == 0

    # Test the area calculation with negative radius
    try:
        area(-1)
        print("Test failed: No exception raised for negative radius.")
    except ValueError:
        print("Test passed: Exception raised for negative radius.")
# Run the test function
test_area_function()
