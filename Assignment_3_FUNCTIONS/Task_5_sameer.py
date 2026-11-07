# Create a list containing product prices
prices = [100, 250, 400, 1200, 50, 2000, 850]

# filter() selects only prices greater than 500
# lambda price: price > 500 checks each price
# list() converts the filtered result into a list
expensive = list(filter(lambda price: price > 500, prices))

# filter() selects prices less than or equal to 500
# lambda price: price <= 500 checks each price
# list() converts the filtered result into a list
cheap = list(filter(lambda price: price <= 500, prices))

# Print the expensive prices
print("Expensive prices:", expensive)

# Print the cheap prices
print("Cheap prices:", cheap)