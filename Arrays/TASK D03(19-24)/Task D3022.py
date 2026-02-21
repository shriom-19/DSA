# find all divisor

def devisors(a):
    
    divs=[]
    for i in range(1,int(a**0.5)):
        if a%i==0:
            divs.append(i)
            divs.append(int(a/i))
    return set(divs)

print(devisors(100))