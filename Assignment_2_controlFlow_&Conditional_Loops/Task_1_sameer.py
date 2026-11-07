order_amount = input("Enter order amount")
if order_amount.isdigit():
    order_amount = int(order_amount)

    if order_amount >= 2000: 
        discount = 15
    elif order_amount >= 1500:
        discount = 10
    elif order_amount >= 1000:
        discount = 7
    else :
        discount = 0
    discount_amount = (order_amount * discount) / 100
    final_amount = order_amount - discount_amount

    print("Order Amount: ", order_amount)
    print("Discount: ", discount, "%")
    print("Discount Amount: ", discount_amount)
    print("Final Amount: ", final_amount)
else:

    print("Invalid input. Please enter a valid order amount.")
        