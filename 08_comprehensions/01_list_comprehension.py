# first of all comprehension short hand trick hoti h kuch bhi krne ke lie 
# basically comprehensions syntax chota krta h 
# iterables pe use krte h jse list, set, tuple, dict
# [expression for item of iterable condition]
# [x for x in items]: ye entire list bnata h memory me 
menu_items = [
    "Masala Chai",
    "Iced Lemon",
    "Green Tea",
    "Ginger Tea",
    "Iced Peach Tea"
]

iced_tea = [tea for tea in menu_items if "Iced" in tea]
# isme jo expression me tea h vo individual jo merko mil rha h loop se vo h 
# diffrent likhunga to error milega 
# loop lgaya and condition jo m chayta hu vo
print(iced_tea)