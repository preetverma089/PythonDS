# set comprehensions list comprehension ki trh bilkul same h but square bracket ki jga curly bracket ayenge
# {expression for item of iterable condition}

# favourite_chais = [
#     "Masala Chai",
#     "Green Tea",
#     "Masala Chai",
#     "Lemon Tea",
#     "Green Tea",
#     "Elaichi Chai"
# ]
# unique_chai = {tea for tea in favourite_chais}
# print(unique_chai)

reciepes = {
    "Masala Chai":["ginger","cardamom","cinnamom","clove"],
    "Elaichi Chai":["cardamom","milk"],
    "Spicy Chai":["ginger","black pepper","clove"]
}
unique_spices = {spice for ingredients in reciepes.values() for spice in ingredients}
print(unique_spices)