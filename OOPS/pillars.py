#              OOP
#               │
#      ┌────────┼────────┐
#      │        │        │
# Encapsulation Inheritance
#      │        │
# Polymorphism Abstraction

# Pillar-1 Encapsulation
# Data or data ke related methods ko unit/class ke andar bundle karna aur access ko control karna

class BankAccount:
    def __init__(self,balance):
        self.balance = balance
   
    def deposit(self, amount):
        self.amount +=amount

    def withdraw(self, amount):
        self.balance -=amount 

# Ye encapsulation ka basic idea hai.
# agar hme attribute ya method ko internal use k lie bnya ho to _ lgake bnta h 
# self._name 
# Internal use ke liye hai; bahar se directly access mat karo.
# __ iska mtlb mangling trigger khte hai

# class User:
#     def __init__(self, name, age,gender):
#         self.name = name
#         self._age = age Protected
#         self.__gender = gender
#     def __study(self):  Private
#         print(self._age)
#         print(self.__gender)



# user1 = User("Preet",34,"Male")
# # print(user1._User__gender)
# user1._User__study()
        
# python me strict ni hote acces modifiers to hm data access kr skte h 
# python me agar single underscore lgaya to hm usko easily use kr skte h and access kr skte h 
#  agar mne double underscore lgaya to directr access ni kr skte uske lie merko _className se acccess krte h jse mne upr kia h 


# Pillar -2 Inheritance

# inheritance: ek class doosri class ke attribute/methods ko inherit kar sakti h 

# class Animal:
#     def eat(self):
#         print("eating")

# class Dog(Animal):
#     pass

# d1 = Dog();
# d1.eat()
# isme kya ho rha h animal class bni usme ek method h then mne ek or class bnyi jo Animal classs se inherit huuii h 
# to by default Animal class ke srre methods, attributes by default child class m aa jte h 

# class Animal:
#     def eat(self):
#         print("eating")

# class Dog(Animal):
#     def bark(self):
#         print("Barking")


# d1 = Dog()
# d1.eat()
# d1.bark()

# isme kya ho rha h ki dog class animal class se inherit huii h 
# uske pass parent class k methods h or vo khud m methods bhi bna skta h 


# Method overriddding:
# isme child class parent class ke methods ke behaviour ko change kr skta h khud k according bss naam same rhta h 

# class Animal:
#     def eat():
#         print("eating")

# class Dog(Animal):
#     def __init__(self,name):
#         self.name = name
#     def eat(self):
#         print(self.name, "eating")


# d1 = Dog("Pug")
# print(d1.name)
# d1.eat()

# super Keyword
# agar child ko parent ka method call krna ho

# class Animal:

#     def __init__(self, name):
#         self.name = name


# class Dog(Animal):

#     def __init__(self, name, breed):
#         super().__init__(name)
#         self.breed = breed


# d1 = Dog("jacky", "PUG")
# print(d1.breed)
