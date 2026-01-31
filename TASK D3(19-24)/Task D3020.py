def factorial(i,r):
    a=1
    for n in range(i-r+1,i+1):
        a*=n
        
    return a

print(factorial(6,3))
