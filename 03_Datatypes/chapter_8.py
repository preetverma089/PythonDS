# List in python 
# they are mutable because they are changeable
# jb hm ek variable me list bnate h thn dusri list bnate h to uska refrence change ho jta h 
# in python array call list

ingredients = ['water', 'milk', 'black tea']
# agar ye tuple hota to hmne ek br bnaya to usme value change ni kr skte 
# but list me hm add, delete kr skte h 

# append element ko last me add kr dega
print(F" ingredients before adding {ingredients}")
ingredients.append("cardamom")
print(F" ingredients after adding {ingredients}")

# Extend Method: ye multiple values or list k andar list store krta h 
# spice_mix = ["Cloves","Ginger"];
# ingredients.extend(spice_mix);
# print(F"adding two arrays{ingredients}")

# Insert Method: iska kaam h special index pe element store krta h 

# insert element at given index list.insert(index, element);
# insert index pe jo element hoga vo right shift hoga
# ingredients.insert(3, "Coffee")
# print(F"inserting element at given index{ingredients}")

# Pop Method: ye element elementm ko remove krne ke lie hota h

# pop: element ko remove kr dega and ye hme deta bhi h konsa element remove hua h agr vo variable me initailised h to
# last_added= ingredients.pop();
# agar pop me index dia usko remove kr dega by default last ko krta h 
# print(F"last element removed {last_added}")
# print(F"list after removed last element{ingredients}")

# Reverse Method: list ko reverse krne k lie hm reverse method ka use krte h
#  
# reverse complete list
# ingredients.reverse()
# print(F"list after reversed {ingredients}")

# sort method sorts list as per alphabatically
# print(F"list before sorted{ingredients}")
# ingredients.sort()
# print(F"list after sorted{ingredients}")

# Remove Method: ye duplicatee values h to unko remove kr deta h first occurence ko remove kr deta h  
# nums = [10, 99, 20, 30, 20]
# nums.remove(20)
# print(nums)

# Clear Method: ye puri list ko empty kr deta h 
# clear();
# nums = [10,20,30,50]
# nums.clear()
# print(nums)

# Index Method: ye hme element ka index return krke deta h 
# nums= [10,20,30,40]
# print(nums.index(30))
# duplicate values me first occurence ka index deta h 

# count: ye hme element ka count deta h 
# nums = [10,20,30,20,20,50]
# print(nums.count(20))

# sugar_level = [1,2,3,4,6]
# print(F"maximum sugar level is {min(sugar_level)}")


# Sort Method: ye elements ko by default ascending order me sort krke deta h 
# nums = [40, 10, 30, 20]
# nums.sort()
# nums.sort(reverse=True) ye descending order me sort krke deta h 
# print(nums)
# ye orginial list ko change krta h 

# Sorted Method: ye new list sort krke deta h ascending or descending
# nums = [40,20,60,30]
# new_Nums= sorted(nums) by default ascending order
# new_Nums= sorted(nums,reverse=True) descending order
# print(new_Nums)


# Length: ye list ki length nikal ke dta h hme
# print(len(nums))


# Copy Method: ye ek list se dusri list bna deta hb 
# isme deep copy shallow copy vala concept nhi hota 
# nums = [10,20,30,40]
# new_nums =nums.copy()
# print(F"new Nums is {new_nums}")
# print(F"new Nums is {nums}")
# copy module ko import krke deep copy kr skte h 



# ----------------------------------->>>>>>>>>>>>>>>___________________--------

# operator overloading
# Iska mtlb ye h ki jse plus operator ka kaam diffrencr object me diffrent hota h 
# jse integers + integers to sum, string + string = string concatenation, list + list = list concatenation 
# python me operators use krte time intertnally dunder method use krtaa h 
# example for dunder methods: a + b similar to a.__add__(b)
# base_liquid = ["water",'milk']
# extra_flavour = ['ginger']

# total_falvours = base_liquid + extra_flavour
# print(F"operator overlaoding {total_falvours}")


# storm_brew = ["black tea"] * 3 
# # ye array ke element ko multiply krke three time kr dega ["black tea", "black tea", "black tea"]
# print(F"storm_brew{storm_brew}")


# python me byteArray and bytes basically dono binary data store karte hain, yani values 0–255 ke range me hoti hain.
# byteArray basically mutable hota h and bytes hmara immmutable hota h
# bytearray tab useful hota hai jab tumhe binary/raw data ko modify karna ho.

# For example:

# Files ke binary data ko manipulate karna
# Network data/buffers
# Images/audio/video ke raw bytes ke saath kaam karna
# Encryption/decryption related processing
# Performance-sensitive byte manipulation


# # convert string into list
# str = "CINNAMON"
# # byteArray() is used for converting into list

# raw_spice_data = bytearray(b"CINNAMON")
# print(F" byteArray {raw_spice_data}")

#  To be revised again
