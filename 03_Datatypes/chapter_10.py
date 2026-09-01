# Dictionary 
# Python me dict ek key-value data structure hai.
# it stores data not in index it stores data in format of name
# Ek naam/key do aur uske against koi value store kar do.
# dict me keys unique honi chyiye nhi to same keys override ho jti h 
# city = "charkhi Dadri"
# user_dict = {
#     "name":"Preet",
#     "age":31,
#     "gender":"male",
#     "mobile":9812050005,
#     "city":city
# }
# dict me key ki value kio bhr se aaya hua variable bhi ho skta h and jo last assignment wins
# value duplicate ho skti h 
# print(user_dict)
# Dictionary keys hashable honi chahiye kuuu ki dict hashing support krti h to keys  bhi hashable honi chyiye
# list [1,2,3] ye hashable ni h ye kbhi bhi dict ki key nhi bn skti 
# data = {
#     "name": "Prince",
#     10: "hello",
#     True: "yes",
#     (1, 2): "tuple"
# }
# Dictionary internally kaise kaam karti hai?
# student = {
#     "Prince": 25,
#     "Preet": 26
# }
# Python internally hashing ka use karta hai.
# "Prince"
#    ↓
#  hash("Prince")
#    ↓
#  hash value
#    ↓
#  appropriate location/bucket
#    ↓
#  25
# jbb user search krta h student["Prince"]
# ese dhundta h value ko
# phle search key ko hash krta h phr uske bddd ek value milti h usse vo bucket tk jata h uske bdd uss value number se dhund lega key ki value
# "Prince"
#    ↓
# hash
#    ↓
# location
#    ↓
# 25
# Isliye dictionary lookup average case me O(1) hota hai.
# agar key nhi h to key error throw krta h 
# dict ko bnane k 2 trike h ek dict() isse and ek direct
# get method use krke value le skte ha :- student.get("keyName"); agar key exist hogi to value mil jyegi ni to None milega
# print(student.get("city", "unknown")) isme agar key ni mili to default value de dega hme (Real World Projects me bhuut use hota h)
# Dictionary me value add karna: student["age"] = 25;  ese krke hm key value add krte h same syntax se update bhi ho jti h and agar nhi h to add ho jti h 
# Dict me multiple value add krni h uske lie update function use hota h 
# del student["age"]  ye and student.pop(keyName) isse key and value delete ho jti h key value dict se 
# student.pop("gender",None) default value kuu ki agar key ni h to error degi isiliye hm default value set krte h 
# clear function: ye hmari dict ko empty kr dega
# len function: ye hme dict ki key ka count dega
# in Function: ye function hme check krke dega ki key exists krti h ya dict me ya nhi
# dict.key(): ye function hme dict ki srri keys dega usually hm isko loop se nikalte h output: dict_keys(['name', 'age', 'gender', 'mobile'])
# dict.values(): ye function hme values dega srri.. output: dict_values(['Preet', 34, 'male', 9812050005])
# dict.items(): ye hme keys and values dono deta h output: dict_items([('name', 'Preet'), ('age', 34), ('gender', 'male'), ('mobile', 9812050005)])
# Nested Dict:-
# student = {
#     "name":"Preet",
#     "age":34,
#     "address":{
#         "city":"ckd",
#         "pincode":127306
#     }
# }
# print(student["address"]["pincode"])
# List in Dict:-
# student = {
#     "name":"Preet",
#     "age":34,
#     "skills":["javascript","python","c#"]
# }
# print(student["skills"])
# Dictionary + List + Dictionary:-
# user = {
#     "id": 101,
#     "name": "Prince",
#     "skills": [
#         {
#             "name": "Python",
#             "experience": 3
#         },
#         {
#             "name": "React",
#             "experience": 2
#         }
#     ]
# }
# print(user["skills"][1]), print(user["skills"][1]["name"])
chai_order = dict(type="Masala Chai",size="Large", sugar = 2)
# print(F"chai order{chai_order}")
#  dictionary me order mattter nhi krta kuu ki hm data ko uski key se access krte h 


# another way to create dictionary

chai_reciepe = {}
chai_reciepe["base"] = "black tea"
chai_reciepe["liquid"] = "milk"
chai_reciepe["ingredients"] = ["Ginger", "Cardamom", "Cinnamon"]

# print(F"chai_reciepe {chai_reciepe}")
# print(f"chai_reciepe {chai_reciepe["liquid"]}")

# to delete any key from dictionary 
del chai_reciepe["ingredients"] 

# print(F"chai_reciepe {chai_reciepe}")

# Membership testing
# in Operator return true if key exists otherwise return false
# print(f"is Sugar in the order {"Sugar" in chai_reciepe}")

#  pop method is used to remove key
# values method give all the values in dict 
# print(f"Order details (keys) {chai_order.values()}")
# print(f"after popped sugar{chai_order}")

extra_spices = {"ginger":"sliced", "cardamom":"crushed"}
chai_order.update(extra_spices)
# print(f"chai_order{chai_order}")

# popItem remove last item from dict
last_item = chai_order.popitem()
# print(F"last item{last_item}")
# print(f"chai_order{chai_order}")

customer_note = chai_order.get("note", "NO Note")
# print(F"customer_note {customer_note}")


