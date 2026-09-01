# inside this i use ternary operator
order_amount = int(input("Enter order amount"))
delivery_fees = 0 if order_amount>300 else 30

# isme ternary opertor ese lagta h ki hm initalise krte h if me jo true hoga vo phle thn
# sytnax: if ka result if condition else jo krna h 
print(f"delivery fee is {delivery_fees}")