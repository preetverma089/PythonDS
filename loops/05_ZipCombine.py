# zip is used for use two list paralelly
names = ["Preet","Anu","Hitesh","ALI"]
bills = [50,70,100,55]

for name,amount in zip(names, bills):
    print(f"name and bill amount is {name}: {amount}")