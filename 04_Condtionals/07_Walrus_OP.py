# value = 13
# remainder = value%5

# if remainder:
#     print(f"remainder is {remainder}")


# walrus opeator
# value = 13
# if(remainder:=value%5):
#     print(f"remainder is {remainder}")

# available_Sizes = ["small","medium","large"]

# if(requested_size:=input("enter you size ") in available_Sizes):
#     print(f"serving {requested_size}")
# else:
#     print("size not present")



users = [
    {"id":1, "total":100, "coupon":"P20"},
    {"id":2, "total":45, "coupon":"F10"},
    {"id":3, "total":554, "coupon":"P50"}
]

discount = {
    "P20":(0.2,0),
    "F10":(0.5,0),
    "P50":(0,10)
}

for user in users:
    percent, fixed = discount.get(user["coupon"],(0,0))
    discount = user['total'] * percent + fixed
    print(f"{user["id"]} paid {user["total"]} and got discourn fixed{discount}")