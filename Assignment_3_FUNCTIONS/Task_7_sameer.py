# Create an empty list to store product prices
prices = []


# Function to add a new price to the list
def add_price(prices_list, price):

    # append() adds the given price to the end of the list
    prices_list.append(price)


# Function to calculate the average price
def get_average_price(prices_list):

    # sum() adds all prices
    # len() counts the number of prices
    # Divide total prices by the number of prices
    return sum(prices_list) / len(prices_list)


# Function to find the highest price
def get_max_price(prices_list):

    # max() returns the largest price in the list
    return max(prices_list)


# while True creates an infinite loop
# The menu keeps displaying until we use break
while True:

    # Display the menu options
    print("\n1. Add price")
    print("2. Show average price")
    print("3. Show maximum price")
    print("q. Quit")

    # Get the user's choice as a string
    choice = input("Enter your choice: ")


    # Check whether the user selected option 1
    if choice == '1':

        # Get the price from the user
        # float() allows decimal values
        price = float(input("Enter price: "))

        # Call add_price() to add the price to the list
        add_price(prices, price)

        # Display success message
        print("Price added successfully.")


    # Check whether the user selected option 2
    elif choice == "2":

        # Check whether the list contains at least one price
        if len(prices) > 0:

            # Call get_average_price() and display the result
            print("Average price:", get_average_price(prices))

        else:

            # Display this message if the list is empty
            print("No prices available to calculate average.")


    # Check whether the user selected option 3
    elif choice == "3":

        # Check whether the list contains at least one price
        if len(prices) > 0:

            # Call get_max_price() and display the highest price
            print("Highest price:", get_max_price(prices))

        else:

            # Display this message if the list is empty
            print("No prices available to find maximum.")


    # Check whether the user selected q
    elif choice == "q":

        # Display exit message
        print("Exiting the program.")

        # Stop the while loop
        break


    # If the user enters anything other than 1, 2, 3 or q
    else:

        # Display an invalid choice message
        print("Invalid choice. Please try again.")