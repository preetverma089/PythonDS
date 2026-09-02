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


# Polymorphism
# Same interface/method name, different objects → different behavior.
class Dog:

    def sound(self):
        print("Bark")

class Cat:

    def sound(self):
        print("Meow")

# means diffrent class but same method but diffrent behaviour

# Duck Typing:- "If it walks like a duck and quacks like a duck, treat it like a duck."

# Pillar 4: Abstraction
# Complex internal implementation hide karo, user ko sirf necessary interface dikhao.
# hm car usen krte h Start, Brake, Accelerate, Steering ye hme dikhta h 
#  engine k andar fule injection, combustion, pistons, crankshaft, transmission

# kaise work kar rahe hain, har baar jaanne ki zarurat nahi. it is called abstraction
from abc import abc, abstractmethod

class Animal(abc):
    @abstractmethod
    def sound(self):
        pass

class Dog(Animal):

    def sound(self):
        print("Bark")

# agar parent class me method abstract kr rkha h to child class ko uska implementatiojn provide krna hoga 
# @abstractmethod
# def sound(self):
#     pass

# Payment
#    │
#    ├── Razorpay
#    ├── Stripe
#    └── PayPal

# class Payment(ABC):

#     @abstractmethod
#     def pay(self, amount):
#         pass

# pay() every payment provider ko pay method implement krna hoga
# But internally payment kaise process hota hai, caller ko nahi pata.

# Class Variable VS Instance Variable

# Instance Variable 
# class User:

#     def __init__(self, name):
#         self.name = name

# Har object ka apna:

# user1.name
# user2.name

# Class Variable

# class User:
#     company = "ABC TECHNOLOGIES"

# Ye class ke saath associated hai.
# All instances can access it:
# user1.company
# user2.company

# means ki instance variable me hr object ka variable diffrent hota h but class variable me class me variable set krte h to jo jo instnce us clss se bnega usme automatic aa jyega

# Instance Method:

# class User:
#     def login(self):
#         print("Login")
    
# class Method

class User:
    company = "ABC TECH"

    @classmethod
    def get_company(cls):
        return cls.company

# yha pe cls current class ko refer kr rha h 
# self current object ko refer krta h and cls current class ko refer krta h 

# Static Method
# @staticmethod :Static method basically class ke namespace ke andar logically related function hai

# class Math:

#     @staticmethod
#     def add(a, b):
#         return a + b
# Isme cls and self ki need ni hoti
# utility helper k lie use krte h hm isko

# Kabhi-kabhi class ke andar hume aisa function banana hota hai jo:

# object ke data ko use nahi karta
# class ke data ko bhi use nahi karta
# bas logically class se related hai

# Tab hum @staticmethod use kar sakte hain.
# class Calculator:

#     @staticmethod
#     def add(a, b):
#         return a + b

# Property
# kya hota h ki by default instance method self use krta h to hme property/attribute bnane ki need ni hoti
# but some case me merko property ki need hoti h to @proprerty bnata hu jo dikhta to function ki trh but hota h attribute/Property

# class User:

#     def __init__(self, email):
#         self._email = email

#     @property
#     def email(self):
#         return self._email
# access krte h isko u1.email attribute ki trh

# Setter: Property ko controlled way se modify bhi kar skte ho
class User:

    def __init__(self, email):
        self._email = email

    @property
    def email(self):
        return self._email

    @email.setter
    def email(self, value):

        if "@" not in value:
            raise ValueError("Invalid email")

        self._email = value
# This is a common encapsulation pattern.


# Dunder Methods
# Python classes ka very important feature 

# __init__
# __str__
# __len__
# __eq__
#__add__
# Dunder = double underScore

# isA and Has_A relation:
# Mtlb ek class dusri class se related h IS A 
# ek object me dusra object h HAS A
# IS A : Inheritance and 
# HAS A: composition