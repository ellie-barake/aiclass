def temp_converter():
    temp_c=float(input('enter temp_c'))
    temp_f= (temp_c * 9/5) +32
    print(f'{temp_c}C = {temp_f:.1f}F')

def calculate_discount():
    cost=float(input("enter the cost"))
        if cost > 100:
        final= cost * 0.8
    elif cost >= 50:
        final= cost * 0.9
    else:
            final= cost
    cost=float(input("enter the cost"))
    print(f'Discount cost: MK{final}')

def main():
    print("welcome to smart tools!")
    print('1. temprature converter(C to F)')
    print('2. shop discuont callculator')

    choice = input('choose an option(1-2):')
    if choice== '1':
       temp_converter()
    elif choice== '2':
        calculate_discount()
    else:
        print("invalid choice. Try again.") 
main()  
