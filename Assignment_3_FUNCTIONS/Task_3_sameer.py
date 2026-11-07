# Create a lambda function to calculate the price after adding 18% GST
gst = lambda price: price + (0.18 * price)

# Create another lambda function to:
# 1. Accept the original price
# 2. Accept discount percentage (default value is 0)
# 3. Calculate the discounted price
# 4. Pass the discounted price to the gst() function
final_price = lambda price, discount_percent=0: gst(
    price - (price * discount_percent / 100)
)

# Call gst() with price = 1000
# GST of 18% is added to 1000
print("Price after GST:", gst(1000))  # Output: 1180.0

# Call final_price() with price = 1000 and discount = 10%
# First, 10% discount is calculated
# Then, 18% GST is added to the discounted price
print("Final price after discount and GST:", final_price(1000, 10))
# Output: 1062.0