# Tuples 
# () parenthesis use hota h 
# there are immutable
# isme values update hoti h refrence change ni hota
masala_Spice = ("Cardamom","Ginger", "Tea")
# print(masala_Spice.__len__())  ye function tuple ki length dega usme kitne elements stored h 
# print(len(masala_Spice)) ye bhi size dega tuple ka 2
# Destructuring of tuples
# unpack krne k lie isme jitne elements honge utne variables initalize krne honge
# like tuple me 4 h mne 3 ko unpack kia to error aa jyega
# isiliye jitnen tuples me elements h utne variables hone chyiye unpack k lie


# (spice1, spice2, spice3) = masala_Spice;

# print(F"masala : {spice1}, {spice2}, {spice3}")

# Second way to destructure tuples are this:-

# ginger_ratio, cardamom_ratio = 2,1
# print(f"ratio is {ginger_ratio} and {cardamom_ratio}")
# ginger_ratio, cardamom_ratio = cardamom_ratio, ginger_ratio
# print(f"ratio is {ginger_ratio} and {cardamom_ratio}")



# Membership 
# in function to check is that value exists in tuple or not
# ye exact value check krta h isme basically upper case and lower case important hota h known as case sensitive
print(F"cloves exists in masala_spice: {'Ginger' in masala_Spice}")