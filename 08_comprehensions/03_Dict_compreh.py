# {key:value for key,value in dict.items()} 
# dict.items muje dict ki key value deta h 
# dict.keys se keys milti h 
# dict.values se mrko values milti h srri
tea_prices = {
    "Masala Chai":400,
    "Green Tea":500,
    "Lemon Tea":1000,
    "Mix Tea":2000
}

updated_prices = {tea:prices / 80 for tea,prices in tea_prices.items()}
print(updated_prices)