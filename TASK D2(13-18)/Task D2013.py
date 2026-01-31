# triangular number 

def triangular_num( n ):
    sum=0
    for i in range(0,n):
        sum+=(n-i)

    return sum

i=int(input("Enter the num:"))
print(triangular_num(i))
