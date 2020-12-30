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
    print(val)
    print(sum(val))
    print(average(val))
    print(median(val))
    print(min(val))
    print(max(val))


if __name__ == "__main__":
    main()
