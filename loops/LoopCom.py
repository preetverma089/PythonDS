# for and while loop in python 

# users = ["Preet", "Rishi", "Sahil"]

# for variable in iterable:

# for user in users:
#     print(user)

# range(start, stop, step)
# range(start, stop, step)

# step nahi diya → +1
# Aage jaana hai → +1
# Peeche jaana hai → -1

# for i in range(5):
#     print(i)

# for i in range(2,7):
#     print(i)

# for i in range(1,10,2):
#     print(i)


# for i in range(10,0):
#     print(i)

# Now loop with Strings 
# name = "Preet"

# for char in name:
#     print(char)

# tuple k sth
# num = (1,2,3,4)
# for digi in num:
#     print(digi)

# set k saath 
# num = {10,20,30}

# for digi in num:
#     print(digi)

# user = {
#     "name":"Preet",
#     "age":34,
#     "gender":"male",
#     "city":"CKD"
# }
#  keys
# for key in user:
#     print(key)

# values
# for value in user.values():
#     print(value)

# for key,value in user.items():
#     print(key, value)

# # enumerate:
# users = ["preet","azmeen", "arpit"]

# for index, user in enumerate(users):
#     print(index, user)

# zip: isme hm 2 list ko ek sth iterate kr skt eh 
# users = ["preet","azmeen", "arpit"]
# age = [26,23,21]

# for name,age in zip(users,age):
#     print(name,age)

# break keyword

# for i in range(1,10):
#     if(i==5):
#         break
#     print(i)

# continue keyword 
# for i in range(1,10):
#     if(i==5):
#         continue
#     print(i)

# Nested Loops 
# 1: isme ki range fn i-1 tk chlta h
# 2:  next line jaaane se rokne k lie print me end="" ye dalna pdta h 
# for i in range(0,10):
#     for j in range(0,i+1):
#         print("*", end="")
#     print("")

# while loop
# i = 0
# while i<=10:
#     print(i)
#     i+=1

    