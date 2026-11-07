
# Point 1: Create a list of product names
products = ['Apple', 'Banana', 'carrot']

# Create a dictionary containing product prices
price_dict = {
    'Apple': 20,
    'Banana': 10,
    'carrot': 30
}

# Create a list containing product categories
categories = ['Fruit', 'Fruits', 'Vegetables']


# Point 2: Create a catalog containing product details
# Each catalog entry contains (product name, price, category)
catalog = []

# Loop through the product list using index positions
for i in range(len(products)):

    # Get the product name
    name = products[i]

    # Get the price of the product from the dictionary
    price = price_dict[name]

    # Get the corresponding product category
    category = categories[i]

    # Add the product details as a tuple to the catalog
    catalog.append((name, price, category))

# Display the complete product catalog
print("Catalog:", catalog)


# Point 3: Group product names according to their categories
category_to_products = {}

# Loop through each product tuple in the catalog
for product in catalog:

    # Extract the product name from index 0
    name = product[0]

    # Extract the category from index 2
    category = product[2]

    # Create an empty list if the category does not exist
    if category not in category_to_products:
        category_to_products[category] = []

    # Add the product name to its corresponding category
    category_to_products[category].append(name)

# Display products grouped by category
print("Category to Products:", category_to_products)


# Point 4: Find the category containing the maximum number of products
max_category = max(
    category_to_products,
    key=lambda category: len(category_to_products[category])
)

# Display the category with the maximum number of products
print("Category with maximum products:", max_category)

# Display all products belonging to that category
print("Products in that category:", category_to_products[max_category])
