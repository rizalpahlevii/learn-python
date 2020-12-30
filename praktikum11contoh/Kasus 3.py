def count(val):
    return sum(i % 2 == 1 for i in val)

def main():
    val = list(map(int, input().split()))
    print(count(val))

if __name__ == "__main__":
    main()