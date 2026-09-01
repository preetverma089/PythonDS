# generators use krte h memory save krne ke lie
# syntax same h bs parenthesis use honge
# (expression for item in iterable condition)
 # (x for x in items): ye stream ki trh chlta h one by one item deta h for memory optimization 

daily_sales = [5,10,12,7,3,15,8,9]

total_cups = sum(cups for cups in daily_sales if cups>5)
print(total_cups)

# isme hm memory effiecnt method lgake kaam kr skte h isse memory pe effect ni hoga jyda
# isko hm list se krte thn again comprehension lgate to jyda impact hota memory pr