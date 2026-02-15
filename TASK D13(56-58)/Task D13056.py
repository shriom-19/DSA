#Maximum Circular Subarray Sum

def max_subarry(arr):
    res=0
    maximum=arr[0]
    i=0
    minimum=arr[0]
    resm=0
    total=0
    n=len(arr)
    while i<n:
        
        res=max(res+arr[i],arr[i])
        maximum=max(res,maximum)
        
        resm=min(resm+arr[i],arr[i])
        minimum=min(resm,minimum)

        total+=arr[i]

        i+=1

    circular=total-minimum

    if minimum==total:
        return maximum
    
    return max(maximum, circular)


arr=[8, -8, 9, -9, 10, -11, 12]
print(max_subarry(arr))

