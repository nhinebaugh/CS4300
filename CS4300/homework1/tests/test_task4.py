#importing necessary kits
import runpy
import pytest

@pytest.mark.parametrize(
    "price, discount, expected",
    [
        (100, 20, 80),
        (100.0, 20, 80.0),
        (100, 12.5, 87.5),
        (89.99, 12.5, 78.74125),
    ],
)
#function to test the good values
def test_calc_discount(price, discount,expected):
    result = runpy.run_path("src/task4.py")

    calculate_discount = result["calculate_discount"]

    #assertion to check for correctness
    assert calculate_discount(price, discount) == pytest.approx(expected)

@pytest.mark.parametrize(
    "price, discount",
    [
        (-10, 20),
        (100, -5),
        (100, 101),
    ],
)

#function to test the bad values
def test_invalid_vals(price, discount):
    result = runpy.run_path("src/task4.py")

    calculate_discount = result["calculate_discount"]

    #assertion to check for correctness
    with pytest.raises(ValueError):
        calculate_discount(price, discount)

@pytest.mark.parametrize(
    "price, discount",
    [
        ("10", 20),
        (10, "20"),
    ],
)

#function to test bad types
def test_invalid_types(price, discount):
    result = runpy.run_path("src/task4.py")

    calculate_discount = result["calculate_discount"]

    #assertion to check for correctness
    with pytest.raises(TypeError):
        calculate_discount(price, discount)
