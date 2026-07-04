
items = {
    "milk": 50,
    "bread": 30,
    "eggs": 60,
    "rice": 100,
    "sugar": 40,
    "veggies":210,
    "cupa noodles":120,
    "flour":150,
    "biscuits": 50,
    "chips": 50,
    "nachos": 100,
    "jam": 75

}

print("Available items:")
for item, price in items.items():
    print(item, "→", price)

cart = []

product_list = input("Enter products (space separated): ").split()

for product in product_list:
    if product in items:
        cart.append(product)
        print(product, "added")
    else:
        print(product, "not available")

total = 0

for item in cart:
    total = total + items[item]

if total >= 200:
    discount = total * 0.20
elif total >= 100:
    discount = total * 0.10
else:
    discount = 0

print("Cart:", cart)
print("Total:", total)
print("Discount:", discount)
print("Final:", total - discount)