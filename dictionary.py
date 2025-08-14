#creating dictionary
contact_book={'ellie':200,'john':300,'pixie':150,'peter':140}
#looping through dictionary
#loop through values
for values in contact_book.values():    
    print(values)
#loop through key-value
for item,phone_num in contact_book.items():
    print(f'{item}:{phone_num}')