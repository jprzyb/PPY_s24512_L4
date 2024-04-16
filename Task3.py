import math


def __main__():
    n = Input_N()
    m = Input_M()

    print(Calculate_Paths_Count(n, m))


def Calculate_Paths_Count(n, m):
    return math.comb(m + n - 2, min(m - 1, n - 1))


def Input_N():
    while True:
        n = int(input("Enter rows count: "))
        if n > 0:
            return n
        else:
            print("Invalid value. Input must be integer >0!")


def Input_M():
    while True:
        m = int(input("Enter columns count: "))
        if m > 0:
            return m
        else:
            print("Invalid value. Input must be integer >0!")


if __name__ == "__main__":
    __main__()
