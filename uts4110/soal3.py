n = int(input("Inputkan bilangan :"))
for i in range(n):
    i += 1
    res = i**2
    if i == 1:
        print(i, "=", res)
        continue
    kata = (" + "+str(i))*(i-1)
    print(str(i)+kata, "=", res)
