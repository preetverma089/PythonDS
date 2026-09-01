# immutable datatpyes jisme refrence change hota h na ki values
# mutable data types jisme vlaue change ho skti h 

# Mutable = object ko same object ke andar change kar sakte ho.

# Immutable = object banne ke baad usko change nahi kar sakte. Change karoge to Python naya object banata hai.
sugar_amount = 2
print(f"Initial_Sugar_Amount : {sugar_amount}");
sugar_amount = 12
print(f"Second_Sugar_Amount : {sugar_amount}");
print("id of 2: {id(2)}") # agar f nhi lagaya to id of 2: {id(2)} print hoga na ki uska address bcz ye isko string me treat kr rha h na ki variable ke value ko print kr rha h
print(f"Id of 2 :{id(2)}")#id ka matlab hota hai identity, identifier, address of object in memory jiska mtlb h ki har object ka ek unique address hota h memory me jisko hum id() function se check kr skte h
print(f"Id of 12 :{id(12)}")

# everything in python is object
#  To check whether our object or variable mutable or immutable we have to check with identifier
# object have three things:- identity(id, identifier), type, value  
# jb mne sugar_Amount me 2 dala to memory me 2 store ho gya
# jb mne again sugar_Amount me 12 dala to memory me new store huya already jo tha uska address store_Amount se remove ho gya 
# hm yha refrence change kr rhe h na ki value

# Sahil ne changes kie