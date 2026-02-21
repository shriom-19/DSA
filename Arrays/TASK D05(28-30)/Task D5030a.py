#Josephus problem

def lastp(n , k):

    i=1
    ans=0
    arr=[ i for i in range(1,n+1)]

    while(len(arr)>1):
        #kill kth element    
        ans = (ans + k - 1) % len(arr) 
        arr.pop(ans)
    
    return arr


print(lastp(5,2))
        
