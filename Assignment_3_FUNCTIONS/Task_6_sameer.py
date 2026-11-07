# Define a function named process_prices
# It accepts a list of prices as an argument
def process_prices(prices):

    # Apply a 10% discount to every price using map()
    # lambda calculates the discounted price
    # list() converts the map result into a list
    discounted_prices = list(
        map(lambda price: price - (price * 0.10), prices)
    )

    # Filter the discounted prices
    # Keep only prices greater than 100
    # list() converts the filter result into a list
    filtered_prices = list(
        filter(lambda price: price > 100, discounted_prices)
    )

    # Return both lists together
    # First: discounted_prices
    # Second: filtered_prices
    return discounted_prices, filtered_prices


# Call the function with a list of five product prices
result = process_prices([100, 500, 900, 50, 750])

# Print the first returned list (discounted prices)
print("Discounted prices:", result[0])

# Print the second returned list (filtered prices)
print("Filtered prices (greater than 100):", result[1])