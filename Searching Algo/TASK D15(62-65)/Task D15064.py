def find_1s(arr):
    low,high=0,len(arr)-1
    n=len(arr)

    while (low<high):

        mid=low+(high-low)//2

        if arr[mid]==0:
            high=mid-1

        if mid==n-1 or arr[mid+1]!=1:
            return mid+1
        
        if arr[mid]>=1:
            low=mid+1

    return-1

arr= [1, 1, 0, 0, 0, 0, 0]
print(find_1s(arr))

