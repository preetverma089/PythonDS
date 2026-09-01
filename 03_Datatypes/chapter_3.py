# Integers
# black_tea_Grams = 12
# ginger_Grams = 12
# python dono refrence ko same object pe point kr rha h agar value same h to python samne integers ko cache kr leta h 
# jiski vja se ye same show hote h id bhi or value bhii kuu ki ek hi object ko point krte h 
# int ki ek range hoti h -5 to 256 
# a is b value check nahi karta, ye check karta hai ki a aur b exactly same object ko refer kar rahe hain ya nahi.

# black_tea_Grams = 1278
# ginger_Grams = 1278

# print(id(black_tea_Grams)==id(ginger_Grams))
# print(id(black_tea_Grams))
# print(id(ginger_Grams))

# total_Grams = black_tea_Grams + ginger_Grams
# print(f"total base grams for tea is {total_Grams}")

# remaining_tea_Grams = black_tea_Grams - ginger_Grams
# print(f"remaining_tea_Grams {remaining_tea_Grams}")

# # division is little complicated in python using / for value(it could be in decimal) but if i use // it gives only integer not decimal values...

# milk_tub = 7
# serving_per_person = 4

# python me divison / use krte h tb decimal value deta h agar hme exact or approx amount chyiye hota h tbb // lgana hota h ussse hme milta h approx value 
# total_serve = milk_tub // serving_per_person
# print(f"milk per serving is {total_serve}") 
# # basically / decimal values dega and // approx values dega

cadamoms_pods = 10
pods_cup = 3
 
#  isme kya hota h ki usually jb muje remainder ki need hoti h tb merko modulo ka use krna hota h 
left_pods = cadamoms_pods %  pods_cup 
print(left_pods)


# cadamoms_pods = 10
# pods_cups = 3
# left_over_pods = cadamoms_pods // pods_cups
# print(f"leftover pods is {left_over_pods}")

# flavour_pods = 2
# color_pod = 3

# ye power ke lie use hota h    

# powerful_pods = flavour_pods ** color_pod

# print(f"powerful_pods is {powerful_pods}")

# total_Amount = 10_000_000_000_000
# print(f"total amount {total_Amount}") ye hm use krte h kuu ki merko reablity k lie billion of number h usko likhna h srf uske lie 