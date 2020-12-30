def average(val):
    return sum(val) // len(val)

def median(val):
    items = len(val) 
    val.sort() 
    if items % 2 == 0: 
        x = val[items // 2] 
        y = val[items // 2 - 1] 
        median = (x + y) / 2
    else: 
        median = val[items // 2] 
    return median

def main():
    val = list(map(int, input().split()))
    
    print(val) # List
    print(sum(val)) # Jumlah
    print(average(val)) # Rata - rata
    print(median(val)) # Median
    print(min(val)) # Nilai minimum
    print(max(val)) # Nilai maksimal

main()