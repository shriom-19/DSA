#divislibe by 4 ,11, 13

def divisibleBy4(n:str):

    n = int(n[-2:])

    return n%4==0

def divisibleBy11(n:str):

    sum1=0
    sum2=0
    for i in n:
        if int(i) % 2==0:
            sum1+=int(i)
        else:
            sum2+=int(i)

    return (sum1-sum2)%11==0

def divisibleBy13(n:str):
    rem=0
    for i in n : 
        rem=(rem+10+int(i))%13

    return rem==0

num=input("enter a long number: ")

print( f" result for divisible 4 is: {divisibleBy4(str(num))}")
print( f" result for divisible 11 is: {divisibleBy11(str(num))}")
print( f" result for divisible 13 is: {divisibleBy13(str(num))}")