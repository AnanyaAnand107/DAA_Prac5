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
            # FIX: Correct indexing for string comparison
            elif X[i - 1] == Y[j - 1]:
                Z[i][j].val = Z[i - 1][j - 1].val + 1
                Z[i][j].dir = 'D'
            else:
                Z[i][j].val = max(Z[i-1][j].val, Z[i][j-1].val)
                if Z[i-1][j].val >= Z[i][j-1].val:
                    Z[i][j].dir = 'U'
                else:
                    Z[i][j].dir = 'S'
    return Z

def printLCS(Z, X, i, j):
    if i == 0 or j == 0:
        return ""

    # FIX: Correct indexing for Z and X
    if Z[i][j].dir == 'D':
        return printLCS(Z, X, i - 1, j - 1) + X[i - 1]
    elif Z[i][j].dir == 'U':
        return printLCS(Z, X, i - 1, j)
    else:
        return printLCS(Z, X, i, j - 1)

def main():
    X = "AGCCCTAAGGGCTACCTAGCTT"
    Y = "GACAGCCTACAAGCGTTAGCTTG"
    m = len(X)
    n = len(Y)
    Z = lcs(X, Y, m, n)

    lcs_length = Z[m][n].val
    lcs_string = printLCS(Z, X, m, n)

    print(f"Length of the LCS is: {lcs_length}")
    print(f"The LCS is: {lcs_string}")
main()