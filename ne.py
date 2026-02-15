print("w x y z f")
for w in range(0,2):
    for x in range(0,2):
        for y in range(0,2):
            for z in range(0,2):
                F = not(y <= (x == z)) and (w <= x)
                if F == True:
                    print(w,x,y,z,F)
               
                