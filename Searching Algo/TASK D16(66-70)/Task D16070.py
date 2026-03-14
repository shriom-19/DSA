## Element with Smaller Left and Greater 

def findmid(arr):

    n=len(arr)
    leftmax=[0]*n

    leftmax[0]=arr[0]

    for i in range(1,n):
        leftmax[i]=max(leftmax[i-1],arr[i])

    rightmin=arr[n-1]

    for i in range(n-2,0,-1):
        if (arr[i]>=leftmax[i-1] and arr[i]<=rightmin):
            return arr[i]
        
        rightmin=min(rightmin,arr[i])

    return arr[-1]


arr = [5, 1, 4, 3, 6, 8, 10, 7, 9]
print(findmid(arr))