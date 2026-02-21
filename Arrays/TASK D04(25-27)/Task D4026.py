#next permutation

def next_permutation(arr):
    n= len( arr )

    pivot=-1

    for i in range(n-2,-1,-1):
        if arr[i]<arr[i+1]:
            pivot=i
            break

    if pivot==-1:
        reversed(arr)
        
    
    for j in range(n-1 , pivot ,-1):
        if  arr[j] > arr[pivot]:
            arr[j],arr[pivot]=arr[pivot],arr[j]
            break

    left, right = pivot + 1, n - 1
    while left < right:
        arr[left], arr[right] = arr[right], arr[left]
        left += 1
        right -= 1

        
arr=[ 2, 4, 1, 7, 5, 0 ]
next_permutation(arr)
print(arr)
    
    
    
    
    
    
        
        
