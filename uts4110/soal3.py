bil = int(input("Inputkan bilangan :"))
for x in range(bil):
    x = x + 1
    res = x**2
    if x == 1:
        print(x, "=", res)
        continue
    yyy = (" + "+str(x))*(x-1)
    print(str(x)+yyy, "=", res)
