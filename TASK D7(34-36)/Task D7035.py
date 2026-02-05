def countSquares(m, n):

    if n < m:
        m, n = n, m

    return (m * (m + 1) * (2 * m + 1)) // 6 + ((n - m) * m * (m + 1)) // 2

m = 4
n = 3
print(countSquares(m, n))