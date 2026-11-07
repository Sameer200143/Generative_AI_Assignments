
# Point 1: Create a list of products
products = [
    "Laptop",
    "Smartphone",
    "Tablet",
    "Headphones",
    "Smartwatch",
    "Webcam"
]

# Display the original product list
print("Original Products:", products)


# Point 2: Create a tuple containing product details
# Tuple format: (Product Name, Price, Category)
sample_product = ("Laptop", 50000, "Electronics")

# Display the sample product details
print("Sample Product:", sample_product)


# Point 3: Access products using list indexing

# Display the second product (index 1)
print("Second Product:", products[1])

# Display the last product (index -1)
print("Last Product:", products[-1])


# Point 4: Add new products to the list

# Add Keyboard and Mouse to the existing product list
products.append("Keyboard")
products.append("Mouse")

# Display the updated product list
print("Products After Adding Keyboard and Mouse:", products)


# Update the price in the sample product tuple

# Convert the tuple into a list because tuples cannot be modified directly
new_sample_product = list(sample_product)

# Update the Laptop price from 50000 to 55000
new_sample_product[1] = 55000

# Convert the list back into a tuple
sample_product = tuple(new_sample_product)

# Display the updated sample product details
print("Updated Sample Product:", sample_product)
