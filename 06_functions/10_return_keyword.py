# def make_chai():
#     print("here is your masala chai")
    # return "here is your masala chai"


# print(make_chai()) dont use this because merko ye dekhna hota h ki return kya hua h isiliye variable vala approach use krte h 
# result = make_chai()
# print(result)

# agar m kuch return ni krta hu to return krne pr None milega
# hm one value, multiple value, early return use krte h function sse return krne par

# def ideal_chaiVala():
#     pass # it gives None object

# print(ideal_chaiVala())

# def sold_cups():
#     return 120

# print(sold_cups())

# def chai_status(cups_left): # isko bolte h early exit from function
#     if cups_left ==0:
#         print('chai cups are empty')
#         return
#     return cups_left;

# result_chai = chai_status(0)
# print(result_chai)

def chai_report():
    return 120, 34 # earning and cups ye merko tuple return krega and usme hm kio bhi data types dal skte h

# print(chai_report())
# ese bhi destructure kr skta hu 

earning, cups = chai_report()
# earning, cups, _ = chai_report() isme underscore lgane se hm jo values hme chyiye vo hi use kr rhe h bkki mne pack hi rkha hua h bina iske krta and return krta 3 vlaues to error aata unpack krne ka 
print(earning)
print(cups)