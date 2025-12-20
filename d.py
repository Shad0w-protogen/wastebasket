def F(N):
    global y
    if N > 0:
        F(N // y)
        print(N % y, end='')

x,y = map(int,input().split())
if x > 0:
    F(x)
elif x == 0:
    print(0)
else:
    print('-',end='')
    F(-x)
    