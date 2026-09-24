#function to calculate a discount
def calculate_discount(price, discount):

    if not isinstance(price, (int, float)):
        raise TypeError("Price must be number")

    if not isinstance(discount, (int,float)):
        raise TypeError("Discount must be number")

    if price < 0:
        raise ValueError("Price cannot be negative")
        
    if discount < 0 or discount > 100:
        raise ValueError("Discount between 0 and 100")

    final_price = price - (price * discount / 100)

    return final_price
