# class ek blueprint/tempalte hoti h 
# class-> user-> name, email, age, login(), logout()
# class ek khud particular user nhi h 
# ye btati h user ke andar kya data or behaviour hoga
# object kys hota h 
# class se actual object bnta h 
# class User:
    # pass 
# user1 = User()
# user2 = User()
# User class -> user1Object -> user2 Object
# user1 and user2 objects/instance hain

# diffrence between class and object
# class Car:
    # pass 
# Object
# car1 = Car()
# car2 = Car()

# Real world Example
# car1 = BMW
# car2 = mercedes
# car3 = audi 
# same class se multiple objects bnnn skte h 
# attributes: Object ka data

class User:
#      User(...)
#    ↓
# __init__(...)
#    ↓
# object initialized
     def __init__(self, name, email):  # basically ye constructor function hota h jb object create hota h tb python automatically initialization krta h 
          self.name = name
          self.email = email
     def Greet(self):
          print(f"name is {self.name} and email is {self.email}")
     def login(self):
          print(self.name, "loggedin")
     def logout(self):
          print(self.name, "logged out")
user1 = User("Prince","2000vermapreet@gmail.com")
print(user1.name)
print(user1.email)
user1.Greet()
user1.login()
user1.logout()
# self keyword: self kla mtlb roughly current object
# jb hm cons bnate h, object bnate h to self means that currnet object
# is object ko refer krega
# same class method diffrent objts k lie kaam kr skta h 
# slef.name vs name
# right side parameter h 
# left side object ka attribute h 
# class k andar functions ko methods khte h 

    #          User Class
    #              │
    #              ↓
    #       new object create
    #              │
    #              ↓
    #     __init__(self, ...)
    #              │
    #              ↓
    #    self.name = "Prince"
    #    self.email = "..."
    #              │
    #              ↓
    #           user
    # Object ke andar data store ho gya

