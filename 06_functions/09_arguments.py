# chai = "Ginger Chai"

# def prepare_chai(order):
#     print(f"Print the order {order}")

# prepare_chai(chai)

# chai = [1,2,3]

# def edit_chai(cup):
#     cup[1] = 43

# edit_chai(chai)
# print(chai)

# jo function declare krne ke time par use hota h use hm parameters bolte h 
# jb hm function call krte h tb jo pass krte h usko hm bolte h arguments

# there are two types of arguments we passed to function
# first denoted by args: jisme hm list, string, anythinh kuch bhi dal skte h 
# secondary is *kwargs as KeywordArgs: 

# def make_chai(tea, milk, sugar):
#     print(tea, milk, sugar)

# make_chai("Darjeling", "Yes","Low") #positional arguments:means muje ye pta h ki first pe kya ayega second pe kya ayega and third pe kya ayega
# make_chai(tea="Green",sugar="Low", milk="Toned") # isme order matter nhi krta isme hm strictly bta rhe h ki konse argument konse parameter se bind hoga isko bolte h keyword_args

# isme *args ye ek tuple return krta h
# isme **extras ye hme dict return krta h
#  dono me hm kio bhi data type dal skte h string, boolean, number, array, everything
# extras behave krta h rest parameter ki trh jo bhi ho last me mil jye 
def special_chai(*ingredients, **extras):
    print("Ingredients",ingredients)
    print("Extras",extras)

special_chai("Cinnamom","Cardmom", sweetner="Honey", Foam="Yes", Milk="Toned")

# default parameter isko bolte h and remember array mutable h agar mne do br call kia to ye usko ki mutate krega and duplicate bhi krega
def chai_order(order = None):
    if order is None:
        order= []
        return
    print(order)

chai_order()
chai_order(["Masala"])

