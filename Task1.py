import math


def __main__():
    n = Input_Matrix_Size()
    Catalan_Number(n)


def Input_Matrix_Size():
    while True:
        n = int(input("Enter a number till which you want to calculate Catalan Numbers: "))
        if n > 0:
            break
        else:
            print("Invalid value. Input must be integer >0!")
    return n


def Catalan_Number(n):
    for i in range(0, n):
        if i == 0:
            cn = 1.0
        else:
            cn = 1 / (1 + i) * Binomial_Theorem(2 * i, i)

        print(i, ": cn: ", cn)


def Binomial_Theorem(n, k):
    return math.factorial(n) / (math.factorial(k) * math.factorial(n - k))


if __name__ == "__main__":
    __main__()
