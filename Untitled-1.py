def sum_some_shit(x,y):
    return (lambda a: lambda b: a + b) (x) (y)

print(sum_some_shit(2,2))