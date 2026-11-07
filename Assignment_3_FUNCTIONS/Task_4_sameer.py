# Create a list containing the original product prices
prices = [100, 250, 400, 1200, 50]

# Create a lambda function to calculate 18% GST
# price is the input parameter
# 0.18 * price calculates 18% GST
# Add GST to the original price
gst = lambda price: price + (0.18 * price)

# map() applies the gst function to every price in the list
# list() converts the map result into a list
price_with_gst = list(map(gst, prices))

# Print the original prices
print("Original prices:", prices)

# Print all prices after adding 18% GST
print("Prices after adding GST:", price_with_gst)