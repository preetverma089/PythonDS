flavour = ["Chcolate","OutofStock","Discontinued","Strawberry"]

for item in flavour:
    if item=="OutofStock":
        continue
    if item=='Discontinued':
        print(f"{item} found")
        break
    print(f"{item} found")
print(f"Outside from loop")
