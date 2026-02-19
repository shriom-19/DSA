#smallest subarray with sum greater than a given 

def smalles_subary(arr,h):
    i,j=0,0
    ressum=0
    ans= float('inf')

    while j<len(arr):

        while j<len(arr) and ressum<=h:
            ressum+=arr[j]
            j+=1

        if j==len(arr) and ressum<=h:
            break

        while i<j and ressum-arr[i]>h:
            ressum-=arr[i]
            i+=1
            
        ans=min(ans,j-i)
        ressum-=arr[i]
        i+=1

    if ans==float('inf'):
        return 0

    return ans 

    
arr = [1, 4, 45, 6, 10, 19]
x =51
print(smalles_subary(arr,51))
