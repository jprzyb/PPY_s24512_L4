def __main__():
    n, d, c = Input()
    Output(mutation(n, d, c))


def Output(c):
    with open("output.txt", "w") as f:
        f.write(c)

def XOR_Genes(a, b):
    if a == b:
        return 0
    return 1


def mutation(n, d, c):
    for i in range(d):
        m_gen = str(XOR_Genes(c[0], c[1]))
        c = c[1:] + m_gen
    return c


def Input():
    with open("input.txt", "r") as f:
        n, d = map(int, f.readline().split())
        c = f.readline().strip()
        if line := f.readline().strip():
            c += line
        return n, d, c


if __name__ == "__main__":
    __main__()
