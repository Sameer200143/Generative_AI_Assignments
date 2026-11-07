# Define a function named factorial that accepts one parameter n
def factorial(n):

    # Check whether the number is negative
    if n < 0:
        print("Negative numbers are not allowed")

        # Stop the function because negative factorial is not allowed
        return

    # Check whether n is 0 or 1
    if n == 0 or n == 1:

        # Factorial of 0 and 1 is always 1
        return 1

    # Multiply n by the factorial of the previous number (n-1)
    # The function calls itself until it reaches 1
    return n * factorial(n - 1)


# Call the function with 5
print(factorial(5))   # Output: 120

# Call the function with 0
print(factorial(0))   # Output: 1

# Call the function with -3
print(factorial(-3))  # Output: Negative numbers are not allowed
                       # Output: None