n = int(input())

for i in range(n) : 
    t = int(input())

    r = 1 
    i = 2
    
    while i <= t :
        r *= i  
        i += 1

    print(r)