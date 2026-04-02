def maxsum(arr):
    n = len(arr)
    
    currsum=sum(arr)
    
    currvalue=0
    for i in range(n):
        currvalue+= i * arr[i]
        
    res=currvalue
    
    for i in range(1,n):
        
        nextvalue=currvalue-(currsum-arr[i-1])+arr[i]*(n-1)
        
        currvalue=nextvalue
        
        res=max(nextvalue,res)
        
    return res

arr = [8, 3, 1, 2]
print(maxsum(arr))
