library_checkout = {"Eragon": "Yes", "Hobbit": "No", "Dune": "Yes", "1984": "No"}

for book, status in library_checkout.items():
    if status == "Yes":
        print(f"{book} is checked out")

print(library_checkout)

print("Hello world")



