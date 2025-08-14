def calculate_discount(cost):
    if cost > 100:
        return cost * 0.8
    elif cost >= 50:
        return cost * 0.9
    else:
            return cost
cost=float(input("enter the cost"))

print(calculate_discount(cost))

def temperature_converter(c)

temp_c=float(input('enter temp_c;'))
temp_f= (temp_c * 9/5) +32
print(f'{temp_c}C = {temp_f:.1f}F')