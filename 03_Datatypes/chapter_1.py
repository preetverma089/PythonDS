# immutable datatpyes jisme refrence change hota h na ki values
# mutable data types jisme vlaue change ho skti h 

# Mutable = object ko same object ke andar change kar sakte ho.

# Immutable = object banne ke baad usko change nahi kar sakte. Change karoge to Python naya object banata hai.
sugar_amount = 2
print(f"Initial_Sugar_Amount : {sugar_amount}");
sugar_amount = 12
print(f"Second_Sugar_Amount : {sugar_amount}");
print("id of 2: {id(2)}")
print(f"Id of 2 :{id(2)}")
print(f"Id of 12 :{id(12)}")

# everything in python is object
#  To check whether our object or variable mutable or immutable we have to check with identifier
# object have three things:- identity(id, identifier), type, value  
# jb mne sugar_Amount me 2 dala to memory me 2 store ho gya
# jb mne again sugar_Amount me 12 dala to memory me new store huya already jo tha uska address store_Amount se remove ho gya 
# hm yha refrence change kr rhe h na ki value

