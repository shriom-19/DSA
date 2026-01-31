def kthDigit(a, b, k):
    mod = 10 ** k
    res = 1
    base = a

    while b > 0:
        if b & 1:
            res = (res * base) % mod
        base = (base * base) % mod
        b >>= 1

    for i in range(1,k):
        res //= 10
    return res

# Driver code
if __name__ == "__main__":
    a = 8
    b = 2
    k = 3
    print(kthDigit(a, b, k))