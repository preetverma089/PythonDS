# enumerate basically kya krta h list ke har item ke saath uska index deta deta h 

menu = ["Green","Lemon","Spiced","Mint"]

for idx, item in enumerate(menu, start=1):
    print(f"enumerate is {idx, item}")