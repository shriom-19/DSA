#prime Factors

def prime_fact(a):
    num=[]
    if a<=1:
        return a
    
    while (a%2==0):
        a/=2
        num.append(2)

    for i in range(3,int(a**0.5)+1,2):
        while (a%i==0):
            a/=i           
            num.append(i)

    if a>2:
        num.append(a)

    return set(num)

print([prime_fact(54)])