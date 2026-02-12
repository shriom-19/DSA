#armstrong num
import math 

n=input("enter any number: ")

def armstrong(n):

    size=len(n.strip())

    output=0

    for i in n:
        output += math.pow(int(i),size)

    return output==int(n.strip())

    
print(armstrong(n))
