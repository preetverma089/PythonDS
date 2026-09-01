
# strings are immutable they can not be change
# inka refrence alag ho jta h 
# chai_category = "Ginger Chai"
# print(f"id of string is {id(chai_category)}")
# chai_category = "Cardamom"
# print(f"id of string is {id(chai_category)}")


# chai_type = "Ginger chai"
# customer_name = "Preet"

# print(F"order for {customer_name} : {chai_type} please !")

# chai_description = "Aromatic and Bold"
# first word kse nikale string se using indexing
# Aromatic and Bold -> indexing starts with 0
# last number not inclusive in case of indexing, slicing in python
# str[start:end:step], 1 in step will be every chracter and if i use 2 then every second chracter will be step and printed
# every second chracter print krega 
# print(F"chai first Word {chai_description[:8:2]}")

chai_description = "Aromatic and Bold"
# print(chai_description[1:])
# print(chai_description[::-2])

# text[8:2:-3] isme ye hota h ki 8 se strt kro 2 tk jao and hr br 3 step piche jao and 3rd vala inclusive hoga 
# print(F"chai first Word {chai_description[12:]}")
# print(F"Reverse complete String {chai_description[::-1]}")


# special Chracter Strings
# hr language k lie special chracters hote h to unke lie string ko encodem and decode krna hota h 
# basically normally hm utf-8 ka use krte h 
# label_text = "Chai Spêćial"
# # print(label_text)
# encoded_label = label_text.encode('utf-8')
# decoded_label = encoded_label.decode('utf-8')
# print(F"normal {label_text}")
# print(F"encoded_label {encoded_label}")
# print(F"Decoded Label {decoded_label}")



# Useful Strings Methods

# text = "hello world"
# text.title()
# text.strip(), text.lstrip(), text.rstrip(), basically spaces ko remove krta h aage or piche se 
# print(text)

# text.upper()
# # "HELLO WORLD"

# text.lower()
# # "hello world"

# text.capitalize()
# # "Hello world"

# text.title()
# # "Hello World"

# text.swapcase()
# "hELLO wORLD"

# text = "preet@gmail.com"  ye string ko split kr dega ya partion kr dega @ se aage or piche se
# print(text.partition("@"))

# text = "Hello World"     # ye given string ka index dega
# print(text.index("World"))

# find and index diffrence  

# text = "hello"
# print(text.find("xyz"))  agar string me substring nhi h to -1 dega 
# print(text.index("xyz")) but index jb find krte h agar nhi mila to value error dega key diffrencen h ye 

# Check Chracter Type Methods
# print("123".isdigit())  check krega ki string me srre integers h ya nhi 1 to soo onn
# print("abc".isalpha()) check krega string me alphabets h kya srre, alphabets means a to z
# print("123ac".isalnum()); ye check krega ki string me alpha nmumeric h ya nhi, alphanumeri means jisme number and alphabets dono ho
# print("hello".islower()) lower case and uppercase check krne ke lie string me 
# print("Hello World".istitle()) isme title mode check hota h means ki string me hr word capital se strt ho

# split and join
# text = "Preet azmeeen ARpeet"
# print(text.split()) isme string ko given condition k according tod deta h 

# join 
# fruits = ["apple", "banana", "mango"]
# print(" - ".join(fruits))  ye join krne ka kaam krta h given string ko condtionaly

# Replace string
# text = "I LOVE JAVASCRIPT"
# print(text.replace("JAVASCRIPT","PYTHON"))

# Search and check methods 
text = "Hello World"
# print(text.startswith("H")) ye check krta h given conditon se ki starting string given string se matchn krta h ya nhi
# print(text.endswith("d")) ye check krta h given string end jo hmne dia h usse hor hi h ya nhi 
# print(text.count("l")) isme given string me check krta h ki hmari string me vo kitni bar aaya h 
# print(text.__len__())  given string ki length check krta h 
# print(len(text)) ye python built-in function h jo object ki length/number return krta h 