#Minimum increment by k operations to make all equal

def operation(arr, k):
    maxi=max(arr)
    res=0

    for i in range(len(arr)):
        if (maxi-arr[i])%k!=0:
            return -1
        
        else:
            res+=(maxi-arr[i])/k

    return res
    
arr = [21, 33, 9, 45, 63] 
k = 6
print( operation(arr , k))
    
    