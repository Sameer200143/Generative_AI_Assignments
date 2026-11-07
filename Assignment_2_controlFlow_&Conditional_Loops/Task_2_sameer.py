order = [1200, 2500, 800, 1750, 3000]
total_revenue = 0
discounted_orders = 0

for order_amount in order:
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

    total_revenue = total_revenue + final_amount

    if discount > 0:
        discounted_orders = discounted_orders + 1

print("Total Revenue: ", total_revenue)
print("Discounted Orders: ", discounted_orders) 