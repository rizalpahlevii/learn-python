def count(val):
    val = filter(lambda x: x in range(1990, 2020), val)
    return sum(i % 2 == 1 for i in val)


def main():
    val = list(map(int, input().split(" ")))
    print(count(val))


if __name__ == "__main__":
    main()
