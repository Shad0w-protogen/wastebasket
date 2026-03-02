def Vector_addition(a,b):
    return a[0]+b[0],a[1]+b[1]

vector1 = (int(input()),int(input()))
vector2 = (int(input()),int(input()))

vector_lol = Vector_addition(vector1,vector2)
print(vector_lol)