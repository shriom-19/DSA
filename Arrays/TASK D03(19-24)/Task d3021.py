#pascals Triangle

def combination( i , r ):
    product=1
    r=min(r,i-r)
    for n in range(r):

        product*=(i-n)//(n+1)

    return product

n=int(input(" enter the rows: "))
for i in range (n):
    for r in range (i+1):
        print(f"{combination(i,r)}", end=" ")
    print()


