orders = []
while True:
    print("\n1.Add order Amount")
    print("2. Show all orders")
    print("q. Quit")
    choice = input("Enter your choice: ")

    if choice == '1':
        amount = float(input("Enter order amount: "))
        orders.append(amount)
        print("Order added successfully.")

    elif choice == "2":
        for amount in orders:
            if amount >= 1000:
                discount = amount * 0.10
            else:
                discount = 0
            final_amount = amount - discount
            print("Order: ", amount)
            print("Final amount:", final_amount)

    elif choice == "q":
        print("Exiting the program.")
        break
    else:
        print("Invalid choice. Please try again.")
        continue
    