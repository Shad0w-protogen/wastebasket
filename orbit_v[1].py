from math import sqrt as a
def orbitalspeed():
    A = [9.82,float(input("insert radius :"))]
    v = a(A[0] * A[1] )
    print("orbital velocity is", v)
    
while True:
    try:
        orbitalspeed()
    except ValueError:
        print("incorrect input")
        
