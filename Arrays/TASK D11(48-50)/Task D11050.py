## Maximum Subarray Sum - Kadane's Algorithm

def kadane_algo(arr):
    j=0
    res=arr[0]
    maximum=arr[0]
    while j< len(arr):
        
        maximum=max(maximum+arr[j],arr[j])
        res=max(res,maximum)
        j+=1
        
    return res

arr = [2, 3, -8, 7, -1, 2, 3]
print(kadane_algo(arr))

