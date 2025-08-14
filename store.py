stock_in_stores={'fanta':6,'bread':4,'shooter':58,'ice':7,'apple':3,'sweets':0,'books':34,'pens':5,'soap':8,'nails':9,'wood':10,'aeroplane':7,'atom':1,'fire':3,'water': 15}
stock_in_stores['wire']= 14
# update an existing stock
stock_in_stores['apple']= 12
stock_in_stores.pop("sweets")
print(stock_in_stores)
#stock_quantity > 5

print("stock which is > 5 in stores")
for stock, quantity in stock_in_stores.items():
    if quantity > 5:
        print(stock)
        # removing
new_quantity={} 
for stock,quantity in stock_in_stores.items():
    if quantity > 0:
        new_quantity[stock]=quantity
print(new_quantity)

total=sum(new_quantity.values())
print(total)







