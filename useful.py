
def transform_number(n):
    binary = bin(n)[2:]  

    if n % 2 == 0: 
        if len(binary) >= 2:
            last_two = binary[-2:]
        else:  
            last_two = binary.zfill(2) 
        transformed_binary = binary + last_two
    else: 
        transformed_binary = '1' + binary + '1'

    result = int(transformed_binary, 2)
    return result

for i in range(70):
    if transform_number(i) > 70:
        print(i)
        break  