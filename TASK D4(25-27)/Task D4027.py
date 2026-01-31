def SieveOfEratosthenes(n):
    isPrime = [True] * (n + 1)
    isPrime[0] = isPrime[1] = False

    for p in range(2, int(n**0.5) + 1):
        if isPrime[p]:
            for i in range(p * 2, n + 1, p):
                isPrime[i] = False

    return isPrime

# Prints all super primes less than or equal to n.
def superPrimes(n):
    isPrime = SieveOfEratosthenes(n)
    primes = [i for i in range(n + 1) if isPrime[i]]
    ans = []

    for k in range(len(primes)):
        if k + 1 < len(isPrime) and isPrime[k + 1]:
            ans.append(primes[k])

    return ans

print(superPrimes(100))