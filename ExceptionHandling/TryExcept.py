chai_menu = {"masala":30, "ginger":40}

# print(chai_menu["elaichi"]) KeyError: 'elaichi'
# ab in sbko handle krne ke lie hm use krte h try, except, else block

# try, except, else, finally blocks hote h code koi run krne ke lie 

# try:
#     chai_menu["eliachi"]
# except KeyError:
#     print("The key that you are trying to access does not exists")     

# print("hello")

# diffrence betweeen exception and error: ye important h 
# Syntax Error: code ka syntax galat h to poython bolega syntax error ye h error
# but exception ka means h ki code syntacally correct hai, lekin execution k time pe problem aa gyii x = 10/0 Zero Division Error ye h exception

# Syntax Error: Code likhne ka rule violate
# Exception: Program run karte waqt problem

# Basic Example:

# try:
#     a = 10
#     b = 0
#     print(a/b)
# except:
#     print("something went wrong")

# try -> exception? -> yes -> except -> continue program
# jse hi error aaya try ka remaining code skip ho jyega and except me chla jyega

# specific exception catch krna ho to ese krte h 

# try:
#     result = 10 / 0
# except ZeroDivisionError: isme hm specific error ko catch kr rhe h isme vhi exception catch hoga jo iss specifc type ka h 
#     print("Cannot divide by zero")

# hm exception object ko bhi access kar skte h 

# try:
#     result = 10 / 0

# except ZeroDivisionError as e:
#     print(e)

# try except else:
# else jbb chlta h jbb try me kio error na aaye
# try:
#     result = 10/ 5

# except ZeroDivisionError:
#     print("something went wrong")

# else:
#     print("code executed sucessfully",result)


# Finally keyword: ye to execute hota hi h chahen kuch bhi ho error aaye ya shii se chle ye execute to hoga hi 
# Ye block almost hamesha execute hoga, chahe exception aaye ya na aaye.
# finally ka kaam h cleanup krna

# try:
#     result = 10 / 5
# except:
#     print("something went wrong")
# else:
#     print("code executred succesfully")

# finally:
#     print("work completed")

# file = open("data.txt", "r")

# try:
#     data = file.read()
#     print(data)

# finally:
#     file.close()


# try:
#     number = int(input("enter your number"))

# except ValueError:
#     print("entered value must be number")

# else:
#     print(number)

# finally:
#     print("work completed")


# Catching Multiple Exceptions:

# numbers = [10,20,30,40]

# try:
#     x = int(input("Entered index: "))
# except ValueError:
#     print("entered value must be number")
# except IndexError:
#     print("Out of index")
# else:
#     print(numbers[x])
# finally:
#     print("work completed")

# multiple exceptions in single except

# numbers = [10,20,30,40]

# try:
#     x = int(input("Entered index: "))
# except(ValueError, IndexError):
#     print("invalid input")
# else:
#     print(numbers[x])
# finally:
#     print("work completed")


# Exception Hiearchy
# BaseException
#     │
#     └── Exception
#           │
#           ├── ValueError
#           ├── TypeError
#           ├── IndexError
#           ├── KeyError
#           ├── ZeroDivisionError
#           ├── FileNotFoundError
#           └── ...

# except Exception: ye bahut sarri normal runtime exceptions catch kar skte h 

# numbers = [10,20,30]


# try:
#     indx = int(input("enter your index: "))

# except Exception as e:
#     print("Error: ", e)

# else: 
#     print(numbers[indx])

# finally:
#     print("work completed")


# Raise : apni tarf se error throw krna

# ab maan lo python technically kio error nahi mil rha lekin business logic ke according tum error generate karna chyate 

# age = 15

# if age<18:
#     raise ValueError("you must be 18 or older")
# else:
#     print("you are adult")

# real world example for this:

# balance = 5000
# withdraw = 7000

# if withdraw > balance:
#     raise ValueError("Insufficient balance")

# balance -= withdraw

# Raise with try except 

# try:
#     age = 15

#     if age < 18:
#         raise ValueError("Age must be 18 or above")

# except ValueError as e:
#     print("Error:", e)


# Custom Exceptions:

# Ab maan lo tum apni application ke specific errors banana chahte ho.
# Python allows you to create your own exception classes.

# Ab ye tumhari custom exception hai.

# class InsufficientBalanceError(Exception):
#     pass

# balance = 6000
# withdraw = 7000

# if withdraw>balance:
#     raise InsufficientBalanceError("insuffiecnt error")


# Custom error ko catch karna 

# class InsufficientBalanceError(Exception):
#     pass

# try:
#     balance = 5000
#     withdraw = 5600
#     if withdraw > balance:
#         raise InsufficientBalanceError("Insuffiect error")
    
# except InsufficientBalanceError as e:
#     print(e)

# else:
#     print("withdraw succesfully")


# Exception me __init__

# Tum custom exception ko data bhi de sakte ho.

# class InsufficeintBalanceError(Exception):
#     def __init__(self,balance, withdraw):
#         self.balance = balance
#         self.withdraw = withdraw
#         super().__init__(f"Balance:{balance}, WithDrawl:{withdraw}")

# try:
#     raise InsufficeintBalanceError(5000,7000)

# except InsufficeintBalanceError as e:
#     print(e)
