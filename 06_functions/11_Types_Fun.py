# Types of Functions in python
# Pure Functions & Impure Functions
# Recursive Functions
# Lambda Functions (Anonymous Functions)


# Pure and Impure Functions

# def chai_cups(cups):
#     return cups * 4

# total_chai = 0

# pure functions vo hote h jo inout mile vsa hi output de, global scope varialbe ya state use na kre
# impure function global scope variable use krte h, output diffrent hota h input se 

# not recommend kuu ki hme global scope variable ko change ni krna chyiye isiliye
# def impure_chai(cups):
#     global total_chai
#     total_chai +=cups

# recursive functions

# def pour_chai(n):
#     print(n)
#     if(n==0):
#         return "all cups are poured"
#     return pour_chai(n-1)

# print(pour_chai(5))


# lambdas functions
# lambda arguments : expression
# expression me return lgane ki need ni hoti
# jb hme single kaam krna ho tb use krte h use sorting, filtering, mapping,quick logic

# chai_types = ['Light',"kadak", "Ginger", "kadak"]

# strong_chai = list(filter(lambda chai:chai=="kadak", chai_types))
# print(strong_chai)
 
# chai_cups = [1,3,4,5,3,3,2,5,3]

# cups_count = list(filter(lambda cups:cups==3, chai_cups))
# print(cups_count)

# sum = lambda a,b: a+b
# mux = lambda a,b,c:a*b*c
# print(mux(5,10,8))