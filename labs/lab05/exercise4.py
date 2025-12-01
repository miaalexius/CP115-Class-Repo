print("Welcome to the Shopping Cost Calculator!")
print("This program will calculate your cost.")

item_name = input("Enter your item name: ")
item_price = float(input("Enter the item price: "))

quantity = 3
tax_rate = 0.06

subtotal = item_price * quantity
tax_amount = subtotal * tax_rate
total_cost = subtotal + tax_amount

print("Total Item: " , subtotal)
print("Tax Amount: " , tax_amount)
print("Total Cost: " , total_cost)
