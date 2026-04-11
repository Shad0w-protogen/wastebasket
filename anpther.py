def transform_to_base3(n):
    def to_base3(num):
        if num == 0:
            return '0'
        digits = []
        while num:
            digits.append(str(num % 3))
            num //= 3
        return ''.join(reversed(digits))

    base3 = to_base3(n)

    if n % 3 == 0:  
        transformed_base3 = '1' + base3 + '02'
    else: 
        suffix_value = (n % 3) * 4
        suffix_base3 = to_base3(suffix_value)
        transformed_base3 = base3 + suffix_base3

    result = int(transformed_base3, 3)
    return result

t = [n for n in range(10000) if transform_to_base3(n) < 100]
    
print(max(t))   