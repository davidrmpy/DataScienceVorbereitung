library = {"Eragon" : 35, "Harry Potter": 55, "Herr der Ringe": 88}

library.update({"Eragon": 40, "Gregs Tagebuch": 22})



print(library)
print(f"The price of Eragon is {library['Eragon']} CHF")
print(f"The price of Gregs Tagebuch is {library['Gregs Tagebuch']} CHF")
print(library.get("Dune", "Not found"))