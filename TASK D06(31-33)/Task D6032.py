#Largest power of k in n! (factorial) where k may not be prime
import math

def factorial(n):
    if (n<=1): return 1
    return n*factorial(n-1)

def check(n,k):
    fact=factorial(n)
    i=1

    while (fact%math.pow(k,i) == 0 ):
        i+=1
    
    return i-1

print(check(n = 10, k = 9))
