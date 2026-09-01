# python function syntax 
# def function_name(parameters):
#     # function body
#     # return value (Optional)
# conceptually fucntion tuple return krta h 
# name = "Preet"
# gender = "male"

# def printName(name, gender):
#     print(f"name: {name}, gender: {gender}")

# def addNumber(num1, num2):
#     return num1 + num2

# sum = addNumber(5,11)
# print(sum)
# printName(name,gender)

# defaullt parameters 
# def greet(name="Guest"):
#     print(name);

# greet()
# agar mne function ko kio argument nhi dia to automatically default utha lega

# def user(name, age, city):
    #   print(name,age,city)

# user("Prince", 34, "ckd")
# isme order matter krta h nhi to mis match ho jyega
# but python hme support krta h ki hm strucure krke function ko arguments pass kr skte h 
# user(name:"Prince",city="ckd",age=34)
# positoonal phle aate h phr keyword arguments aate h 
# default parameter last me aata h 

# def sum_Number(*number):
# number ye tuplers deta h 
#     sum = 0
#     for num in number:
#         sum +=num
#     print(sum)

# sum_Number(10,20,30,40,50,60)

# def create_user(**kwargs):
# kwargs:m iska type dict hota h 
#     print(kwargs)

# create_user(
#         name="Prince",
#         age=25,
#         city="Delhi"
#     )

# def add(a: int, b: int) -> int:
#     return a + b

# def find_user(user_id: int) -> str | None:
# python me function ke andar bnya hua variable uske local scope me bind rhta h
# python global scope variables ko read kr skta h 
# python me agar global scope variables ko modify krna h to global keyword se krte h generally hm isko avoid krte h 
# mne ek function bnaya usko kisi variable me pass kr dunga as object then uss variable ko call krna hota h kuu ki function ka refrece new variable k pass hota h 
# example:- 
#  def greet():
    #    print("name")

# x = greet
# x()
# function ko dusre function ke arguments me pass bhi kr skte h iskom hm bolte h first class function
# def greet():
#     print("Hello")

# def execute(function):
#     function()

# execute(greet)
# function as argument function le ya return kre function usko bolte h higer order functions
# def execute(func):
#     return func()

# lambda Functions:
# small anonymous function 
# square = lambda x:x*x
# print(square(5))
# lambda function ka use hm basically short expression k liem krte h 
# users = [
#     {"name": "Prince", "age": 25},
#     {"name": "Preet", "age": 22},
#     {"name": "Rahul", "age": 30}
# ]

# sorted_users = sorted(users, key=lambda user:user["age"])
# print(sorted_users)
# Function arguments are object references