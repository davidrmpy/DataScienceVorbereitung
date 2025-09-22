cart = {"apple": 5, "laptop": 999, "cake": 12 , "pencil": 1}

for item, price in cart.items():
    if price >= 10:
        print(f"{item} costs {price} CHF")

print(cart)