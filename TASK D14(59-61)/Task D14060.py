#smallest in arry

def samllestinarr(arr):
    low=0
    high=len(arr)-1

    while (low<high):
        mid=low+(high-low)//2

        if arr[mid]==mid:
            low=mid+1

        else:
            high=mid-1

    return low

arr = [0, 1, 2, 3, 4, 5, 6, 7, 10]
print(samllestinarr(arr))