# set comprehensions list comprehension ki trh bilkul same h but square bracket ki jga curly bracket ayenge
#how set internally works:-
# Ram ke ander ek set bna or vo set ek hollow space hota hai or us hollow space me hum jo bhi value save krte hai uski ek hash value create hoti hai or ek baar me hum sirf ek value ki hi hash value  store krta hai or jab dusri value aaegi to uski alag hash value store hoti hai  naaki ek hi hash me saari value store ho
# or jab bhi aap koi duplicate value dekhte ho to uski bhi hash value same hogi to python bolta hai ki pehle se hi ek aisi similar hash value exist krti hai so thats why duplicate value aapki stor nhi hogi

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