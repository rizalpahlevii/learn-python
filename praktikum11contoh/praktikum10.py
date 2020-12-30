def panjangString(s) :
    sum = 0
    for char in s :
        sum+= 1
    return (sum)

def cariKarakter(s,c):
    if s in c :
        print("ada")
    else :
        print("tidak ada")

def frekuensiKarakter(c,s):
    sum = 0
    for i in range(panjangString(s)) :
        if s[i] == c :
            sum+= 1
    return sum

def cekPalindrom(s):
    temp = False
    p = s [ : : - 1]
    if p == s :
        temp = True
    return temp

def main() :
    data = 'balonku ada lima, rupa-rupa warnanya'
    c1 = input()
    c2 = input()
    p = input()
    print(panjangString(data))
    cariKarakter(c1,data)
    print(frekuensiKarakter(c2,data))
    if cekPalindrom(p):
        print("palindrom")
    else:
        print("bukan palindrom")
        
if __name__ == '__main__' :
    main()