#Catlan Number 

def combinations(i , r ):
    res=1
    r=min(r , i-r)
    for n in range(r):

        res=res*(i-n)//(n+1)

    return res

def catlan_nums(n):
    for i in range(n):
        print(combinations(2*i , i )//(i+1))

catlan_nums(4)
    