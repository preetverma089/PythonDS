# comprehensions: iska mtlb h ki kisi bhi iterable ke elements ko loop karke naya collection/expression banana compact syntax me
# suppose numbers = [1,2,3,4,5]
# hme har number ka square chayiye
# numbers = [1,2,3,4,5]
# Square_List = []
# for num in numbers:
#     Square_List.append(num * num)

# print(Square_List)
# list comprehension: 
# Square_List = [number * number for number in numbers]
# print(Square_List)
# Square_List = [number * number for number in numbers] isko smjhte h kya ho rha h 
# [expression for variable in iterable]
# yani kya banana h vo expression me 
#  kha se lena h iterable se lena h 

# examples
# String bhi iterable h 
# str = "Preet"
# letters = [char for char in str]
# print(letters)

# numbers = [1,2,3,4,5]
# mux = [num * 10 for num in numbers]
# print(mux)

# Range k saath 
# numbers = [1,2,3,4,5,6]

# square = [num + 5 for num in range(1,7)]
# print(square)
# range function number sequence se run krta h or traverse krta h isilise 6 aate hi bhr aa jta h 
#  agar hme aray ke starting index se last index tk jna h to ese lgta h  for i in range(leng(numbers)) ye by default 0 leta h 
# sqaure = [numbers[num] + 5 for num in range(len(numbers))]
# Isme len function hme indexes deta h list items ni deta uske lie hme krna pdta h 
# print(sqaure)
# sum = []
# for num in range(len(numbers)):
#     sum.append(numbers[num] + 5)
# print(sum)

# filtering comprehension ka huge useCase
# ese conditions lgti h isme 
# numbers = [1,2,3,4,5,6,7,8,9]
# [expresion for item in iterable if condition]
# even = [x for x in numbers if x%2==0]  
# print(even)
# numbers me se har x lo, agar x even hai, to x ko result me daal do.
# if yha pe filter h 

# Transformation and filtering
# numbers = [1,2,3,4,5,6,7,8,9]
# updated = [num * 10 for num in numbers if num %2==0]
# print(updated)

# if else in comprehensions 
# numbers =[1,2,3,4,5,6,7,8]
# updated = ["Even" if num %2 == 0 else "Odd" for num in numbers]
# print(updated)
# GOLDEN RULE: agar if last me h to vo h filtering h 
# agar hm number select starting me kr rhe h to transform + filtering


# Set Comprehensions:-
# numbers = [1,2,2,2,3,4,4,4,5]
# unique = {num for num in numbers}
# print(unique)

# even = {num for num in range(1,11) if num%2==0}
# print(even)

# names = ["Preet", "Azmeen","Azmeen","Arpit gandva","Preet"]
# unique_Names = {name for name in names}
# print(unique_Names)


# Dictionary Comporehension
# {key_expression:value_Expression for item in iterable}

# numbers = [1,2,3,4,5]

# num_Dict = {
#     x:x*x
#     for x in numbers
# }
# print(num_Dict)

# users = [
#     {"id":101, "name":"Prince"},
#     {"id":102, "name":"Preet"},
#     {"id":103, "name":"Azmeen"}
# ]

# user_dict = { user["id"]: user["name"]for user in users}
# print(user_dict)

# Dict filtering
# users = {
#     "Prince":25,
#     "Azmeen":21,
#     "Arpit":67
# }

# adult_dict = {name:age
#     for name,age in users.items()
#     if age < 50
# }
# print(adult_dict)

# user = {
#     "name": "Prince",
#     "age": 25
# }

# user_dict = {
#     name:age
#     for name, age in user.items()
# }
# print(user_dict)

# ab krte h dict values ko transform

# prices = {
#     "apple": 100,
#     "banana": 50,
#     "mango": 150
# }

# updated_price = {
#     fruit:price + (price * 10) / 100 
#     for fruit, price in prices.items()
# }
# print(updated_price)

# Generator Expression 
# Generator Expression ka syntax: (expresssion for item in iterable) : diffrence ye h isme hm parenthesis use krte h 
# behaviour bilkul diffrent hai..

numbers = [1,2,3,4,5]

# squares = [num * num for num in numbers]
# print(squares)
# isme python immediatly puri list bna deta h and memory me result sorted h 

squares = (num * num for num in numbers)
# print(squares) output: <generator object <genExp>
# value jb hm mangte h jb deta h 
# print(next(squares)) 1
# print(next(squares)) 4 
# ese memory optimzed hoti h 
# Isko lazy evaluation kehte hain.
# print(list(squares)) ese hm srre mang lete h 
