import random


def __main__():
    DEBUG = False
    if DEBUG:
        Run_With_Debug()
    else:
        Client_Run()


def Client_Run():
    n = Input_Matrix_Size()
    p = int(input("Enter a lower bound for the matrix: "))
    q = int(input("Enter a upper bound for the matrix: "))
    aMatrix = Generate_Matrix(n, p, q)
    lMatrix, uMatrix = Calculate_LU(aMatrix)

    print("\tA")
    PrintMatrix(aMatrix)
    print("=\tL")
    PrintMatrix(lMatrix)
    print("*\tU")
    PrintMatrix(uMatrix)


def Run_With_Debug():
    aMatrix = [[2, 1, -3],
               [-6, -7, 7],
               [4, 10, 1]]
    lMatrix, uMatrix = Calculate_LU(aMatrix)
    # Then L matrix should be:
    # [1, 0, 0]
    # [-3.0, 1, 0]
    # [2.0, -2.0, 1]
    #
    # and U matrix should be:
    # [2, 1, -3]
    # [0, -4.0, -2.0]
    # [0, 0, 3.0]

    print("\tA")
    PrintMatrix(aMatrix)
    print("=\tL")
    PrintMatrix(lMatrix)
    print("*\tU")
    PrintMatrix(uMatrix)


def Init_LU(n):
    L = [[0] * n for _ in range(n)]
    U = [[0] * n for _ in range(n)]
    for i in range(n):
        L[i][i] = 1
    return L, U


def Calculate_LU(A):
    n = len(A)
    L, U = Init_LU(n)

    for i in range(n):

        for j in range(i, n):
            sum1 = sum(L[i][k] * U[k][j] for k in range(i))
            U[i][j] = round(A[i][j] - sum1, 2)

        for j in range(i + 1, n):
            sum2 = sum(L[j][k] * U[k][i] for k in range(i))
            L[j][i] = round((A[j][i] - sum2) / U[i][i], 2)

    return L, U


def PrintMatrix(m):
    for i in range(len(m)):
        print(m[i])


def Input_Matrix_Size():
    while True:
        n = int(input("Enter a 'A' matrix size: "))

        if n > 0:
            break
        else:
            print("Invalid value. Input must be integer >0!")

    return n


def Generate_Matrix(n, p, q):
    matrix = []
    for i in range(0, n):
        row = []
        for j in range(0, n):
            row.append(random.randint(p, q))
        matrix.append(row)
    return matrix


if __name__ == "__main__":
    __main__()
