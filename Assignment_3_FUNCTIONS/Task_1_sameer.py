# Define a function named apply_discount
# price = original product price
# discount_percent = discount percentage (default value is 0)

def apply_discount(price, discount_percent=0):

    # Calculate the discount amount
    # Example: 1000 * 10 / 100 = 100
    discount = price * discount_percent / 100

    # Subtract the discount amount from the original price
    # Example: 1000 - 100 = 900
    final_price = price - discount

    # Return the final discounted price
    return final_price


# Call the function with price = 1000 and discount = 10%
print(apply_discount(1000, 10))  # Output: 900.0


# Call the function with price = 500
# We don't provide discount_percent, so its default value (0) is used
print(apply_discount(500))      # Output: 500.0