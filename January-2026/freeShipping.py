
# Given an array of strings representing items in your shopping cart, and a number 
# for the minimum order amount to qualify for free shipping, determine if the items in 
# your shopping cart qualify for free shipping.

# The given array will contain items from the list below:

# Item	Price
# "shirt"	34.25
# "jeans"	48.50
# "shoes"	75.00
# "hat"	19.95
# "socks"	15.00
# "jacket"	109.95

def free_shipping(cart, min_order_amount):
    prices = {
        "shirt": 34.25,
        "jeans": 48.50,
        "shoes": 75.00,
        "hat": 19.95,
        "socks": 15.00,
        "jacket": 109.95
    }
    
    total = sum(prices[item] for item in cart if item in prices)
    
    return total >= min_order_amount

# Example usage:
cart = ["shirt", "jeans", "hat"]
min_order_amount = 100.00
print(free_shipping(cart, min_order_amount))  # Output: True
