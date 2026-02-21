import math

# prime num check

def isprime(a:int):

    if a <=1:
        return False 
    
    for i in range(2, int(math.sqrt(a))+1):
        if a%i==0:
            return False
        
    return True

a=int (input('Enter nUm: '))

##print(f"{isprime(check)}")

for  i in range(2,a+1):
    if isprime(i):
        print(f"{i} ")
