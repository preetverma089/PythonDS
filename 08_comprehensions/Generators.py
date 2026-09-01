# def  get_numbers():
        # return [1,2,3,4,5];

# numbers = get_numbers()

# function start
#      ↓
# [1,2,3,4,5] create
#      ↓
# return
#      ↓
# function finish
# poori list bana ke return karega.

# Generator kya krta h : Generator me hum 
# Generator me hum yield use krta h 
# def get_numbers():
#     yield 1
#     yield 2
#     yield 3
#     yield 4
#     yield 5
# Ye function normally execute hokar saari values return nahi karta.
# ye hme ek generator object retun krta h 

def get_Number():
    yield 1
    yield 2
    yield 3
    yield 4
    yield 5
numbers = get_Number()
print(numbers)

# yield 1 -> 1 de dia -> Pause
# resume -> yield 2 -> 2 de dia -> Pause
# resume -> yield 3 -> 3 de dia -> Pause
# yeild value ko return bhi krta h or function execution ko pause bhi krta h 
# yeild me values milti h one by one

# generator next se bhi chlta h 