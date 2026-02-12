#prfect square
def perfect_square(n):
    if n==0:
        return True


    odd=1
    while (n>0):
        n-=odd
        odd+=2

    return "Yes" if n == 0 else "NO"

print(perfect_square(50))
