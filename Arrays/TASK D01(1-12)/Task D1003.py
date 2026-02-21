a=int(input(" enter the num:"))
b=int(input(" enter the number to divide:"))

def closes_tnum(a , b):
    n=int(a/b)

    n1= n*b

    if ((a*b)>0):
        n2=( b*(n+1))

    else :
        n2=(b*(n-1))
            
    if ( abs(n-n1)<abs(n-n2)):
        return n1
    return 

max_abs=closes_tnum(a,b)
    


print(f"the valid closest number is : {max_abs}")