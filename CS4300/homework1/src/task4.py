#function to calculate a discount
def calculate_discount(price, discount):
    final_price = price - (price * discount / 100)
    return final_price
#print calls to see result of function
print(calculate_discount(100, 20))
print(calculate_discount(10.0, 20))
print(calculate_discount(100, 15.5))
print(calculate_discount(89.99, 12.5))