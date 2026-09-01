# Booleans
#  True consider hota h 1 
# False consider hota h 0

is_Tea_Boiling = True
stri_count = 5
# when boolean converted into integer automatically called upCasting
total_count = stri_count + is_Tea_Boiling
print(F"total_count {total_count}")

milk_present = -1
# basically boolean se string, 1 or more number se boolean me convert krne pr true aata h rather than none, 0 k lie false hi deta h. 
# minus k case me bhi  true hi deta h 
print(F"milk Present is {bool(milk_present)}")

# logical opeators 

tea_present = True
coffee_present = False

result = not tea_present

# python me and,or and not hm text me likhte h sign use ni krte 
# AND, OR, not
print(result);