def CalculateTotal(cart):
    total = 0
    for item in cart:
        try:
            total += float(item['price'])
        except ValueError:
            print(f"Invalid price for item: {item['name']}")
    return total

def display_total(total):
    print(f"Total price: {total:.2f}")

CART = [
    {'name': 'Item A', 'price': 10.99},
    {'name': 'Item B', 'price': 5.99},
    {'name': 'Item C', 'price': 8.49}  # Corrected the price type to float
]

for item in CART:
    print(f"Item: {item['name']} - Price: ${item['price']}")

shopping_cart_total = CalculateTotal(CART)
display_total(shopping_cart_total)