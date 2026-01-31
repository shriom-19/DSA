#Exactly three Divisor
def primee(n):
    prime=[True]*(n+1)
    prime[0]=prime[1]=False

    for i in  range ( 2,int((n**0.5)+1)):
        if prime[i]:
            for p in range(i*2 , n+1 ,i):
                prime[p]=False
        
    return prime


def countDivisors(n):
    total = 0
    prime = primee(n)
    for i in range(2, int(n**0.5) + 1):
        if prime[i]:
            total += 1
    return total

a= int(input("enter input :"))

print(countDivisors(a))
    