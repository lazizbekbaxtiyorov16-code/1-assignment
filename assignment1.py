
subtotal = 0
dishes = []
for i in range(1, 4):
    name = input(f"Dish {i} name: ")
    price = float(input(f"Dish {i} price: "))
    qty = int(input(f"Dish {i} quantity: "))
    dishes.append((name, price, qty))
    subtotal += price * qty

customer = input("Customer name: ")
has_student_id = input("Has student ID? (yes/no): ").strip().lower() == "yes"
order_time = int(input("Order time (hour, 24h format, e.g. 14): "))

student_discount = subtotal * 0.15 * has_student_id
happy_hour = subtotal * 0.20 * (14 <= order_time <= 17)
large_order = subtotal * 0.05 * (subtotal >= 150000)

main_discount = (student_discount * (student_discount >= happy_hour)
                 + happy_hour * (happy_hour > student_discount))

total_discount = main_discount + large_order
discounted_subtotal = subtotal - total_discount

service_charge = discounted_subtotal * 0.10         
delivery = (subtotal >= 100000) * 15000             

total = discounted_subtotal + service_charge + delivery