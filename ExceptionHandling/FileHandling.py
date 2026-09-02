# python me file ke saath kaaam krne k lie hme open() use krte h

# basic python 

# file = open("data.txt","r")

# data = file.read()
# print(data)
# file.close()

# iska mtlb h ki data.txt file ko read mode me open kro 
# file modes:
# "r" : Read, "w": Write, "a":Append, "x":Create newe File "b": Binary, "t":text

# open("data.txt","w"):- carefully write operation existing file ko overwrite kr skta h 
# open("data.txt","a"):-  iska kaam h existing content ke last me add krna

# withopen: ese hm fn bnake operation kr skte h 

# with open("data.txt","r") as file:
#     data = file.read()

# print(data)
# with context manager ensure karta hai ki block complete hone ke baad file properly close ho.
 
# Read
# with open("data.txt","r") as file:
#     data = file.read()

# print(data)

# readLine(): ek line read krega

# with open("data.txt","r") as file:
#     data = file.readline()

# print(data)

# ReadLines: multiple lines read krega
# with open("/data.txt","r") as file:
#     data = file.readlines()

# print(data) 
# lines ko list k format m dega

# ye file me write krega
# with open("data.txt", "w") as file:
    # file.write("Hello Python")

# Append: ye existing data me last m add kr dega
# with open("data.txt", "a") as file:
#     file.write("\nNew line")


# File handling + exceptHandling Project 

# class FileHandlingException(Exception):
#     pass
# try:
#     with open("data.txt","r") as file:
#         data = file.read()
    
#     if not data.strip():
#         raise FileHandlingException("data not found")

# except FileNotFoundError:
#     print("file not exist")

# except FileHandlingException as e:
#     print(e)

# else:
#     print(data)

# finally:
#     print("work completed")

# agar hme ye check krna h ki current directory konsi h jisme python search kr rha h 
# import os

# print(os.getcwd())