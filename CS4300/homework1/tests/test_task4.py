#importing necessary kits
import runpy
#function to test the int price and discount
def test_integer_price_and_discount():
    result = runpy.run_path("src/task4.py")
    calculate_discount = result["calculate_discount"]
    #assertion to check for correctness
    assert calculate_discount(100, 20) == 80

#function to test the float price and int discount
def test_float_price_integer_discount():
    result = runpy.run_path("src/task4.py")
    calculate_discount = result["calculate_discount"]
    #assertion to check for correctness
    assert calculate_discount(10.0, 20) == 8.0

#function to test the int price and float discount
def test_integer_price_float_discount():
    result = runpy.run_path("src/task4.py")
    calculate_discount = result["calculate_discount"]
    #assertion to check for correctness
    assert calculate_discount(100, 15.5) == 84.5

#function to test the float price and discount
def test_float_price_and_discount():
    result = runpy.run_path("src/task4.py")
    calculate_discount = result["calculate_discount"]
    #assertion to check for correctness
    assert calculate_discount(89.99, 12.5)