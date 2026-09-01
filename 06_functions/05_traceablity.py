def add_vat(price, vat_rate):
    return price * (100 + vat_rate)/100

orders = [100, 150,200]

for price in orders:
    total_Bill = add_vat(price, 10)
    print(f"total bill calculated with vat_rate is {total_Bill}")
