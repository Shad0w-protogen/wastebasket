
def factorial(n):
    
    'Calculate factorial using recursion.'

    if n < 0:
        raise ValueError("Factorial is not defined for negative numbers")
    if n == 0 or n == 1:
        return 1
    return n * factorial(n - 1)

a = int(input("length of the password :"))
b = int(input("How many symbols in the password? :"))
if a < 0 or b < 0:
    print("invalid input")
print(a * factorial(b))