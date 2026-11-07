
# Point 1: Create a dictionary containing product names and prices
price_dict = {
    "Laptop": 1000,
    "Smartphone": 800,
    "Tablet": 600,
    "Headphones": 200,
    "Smartwatch": 300,
    "Webcam": 150
}

# Display the original dictionary
print("Original Product Prices:", price_dict)


# Point 2: Add a new product named Keyboard
price_dict["Keyboard"] = 100

# Display the dictionary after adding Keyboard
print("After Adding Keyboard:", price_dict)


# Point 3: Add a new product named Mouse
price_dict["Mouse"] = 50

# Display the dictionary after adding Mouse
print("After Adding Mouse:", price_dict)


# Point 4: Remove a product from the dictionary
product_name = "Webcam"

# Check whether the product exists in the dictionary
if product_name in price_dict:

    # Remove the product if it exists
    del price_dict[product_name]

    print(f"{product_name} has been removed from the dictionary.")

else:
    # Display a message if the product does not exist
    print(f"{product_name} is not found in the dictionary.")


# Point 5: Calculate the total price and average price
# Get the sum of all product prices
total_price = sum(price_dict.values())

# Count the number of products
number_of_products = len(price_dict)

# Calculate the average price
average_price = total_price / number_of_products

# Display the average price
print("Average Price of Products:", average_price)


# Point 6: Find the highest and lowest product prices
max_price = max(price_dict.values())
min_price = min(price_dict.values())

# Display the products with the highest and lowest prices
for name, price in price_dict.items():

    # Check whether the current product has the highest price
    if price == max_price:
        print("Product with the Highest Price:", name, "| Price:", price)

    # Check whether the current product has the lowest price
    if price == min_price:
        print("Product with the Lowest Price:", name, "| Price:", price)
