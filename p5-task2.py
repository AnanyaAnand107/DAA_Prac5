class Cell:
    def __init__(self, val=0, dir=''):
        self.val = val
        self.dir = dir


def lcs(X, Y, m, n):
    Z = [[Cell() for _ in range(n + 1)] for _ in range(m + 1)]

    for i in range(m + 1):
        for j in range(n + 1):
            if i == 0 or j == 0:
                Z[i][j].val = 0
                Z[i][j].dir = 'H'
            # IMPORTANT: add i != j condition
            elif X[i - 1] == Y[j - 1] and i != j:
                Z[i][j].val = Z[i - 1][j - 1].val + 1
                Z[i][j].dir = 'D'
            else:
                if Z[i - 1][j].val >= Z[i][j - 1].val:
                    Z[i][j].val = Z[i - 1][j].val
                    Z[i][j].dir = 'U'
                else:
                    Z[i][j].val = Z[i][j - 1].val
                    Z[i][j].dir = 'S'
    return Z


def printLCS(Z, X, i, j):
    if i == 0 or j == 0:
        return ""
    if Z[i][j].dir == 'D':
        return printLCS(Z, X, i - 1, j - 1) + X[i - 1]
    elif Z[i][j].dir == 'U':
        return printLCS(Z, X, i - 1, j)
    else:
        return printLCS(Z, X, i, j - 1)


def main():
    S = input("Enter a string: ")   # <-- take input from user
    n = len(S)
    Z = lcs(S, S, n, n)

    lrs_length = Z[n][n].val
    lrs_string = printLCS(Z, S, n, n)

    print(f"Length of the LRS is: {lrs_length}")
    print(f"The LRS is: {lrs_string}")


main()
