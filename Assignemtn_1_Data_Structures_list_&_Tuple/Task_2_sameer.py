
# Point 1: Create a list of product categories
categories = [
    "Electronics",
    "Accessories",
    "Electronics",
    "Furniture",
    "Electronics",
    "Accessories"
]

# Point 2: Convert the list into a set
# A set stores only unique values (duplicates are removed)
categories_set = set(categories)

# Display the unique categories
print("Unique Categories:", categories_set)


# Point 3: Add a category to the set
# Adding an existing value does not create a duplicate
categories_set.add("Electronics")

# Display the set after adding Electronics
print("Categories After Adding Electronics:", categories_set)


# Point 4: Check whether a category exists in the set

# Check if Electronics is present
print("Is Electronics available?", "Electronics" in categories_set)

# Check if Clothing is present
print("Is Clothing available?", "Clothing" in categories_set)


# Point 5: Count the number of unique categories
print("Number of Unique Categories:", len(categories_set))
