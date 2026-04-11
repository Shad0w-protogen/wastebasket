def cuck(a):
    a = oct(int(a)).replace("0o",'')
    return a 

def has_even_around_4(s):
    import re 
    # Pattern: even digit + 4, OR 4 + even digit
    pattern = r'[02468]4|4[02468]'
    return bool(re.search(pattern, s))

t = [i for i in range(10000,100000) if has_even_around_4(cuck(i)) == False and str(i)[0] in ('2','4','6','8')]
print(len(t))