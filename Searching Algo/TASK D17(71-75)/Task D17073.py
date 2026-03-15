#Find a Fixed Point (Value equal to index) in a given array

def fixedpoint(arr):

    high=len(arr)-1
    low=0

    while low<high:
        mid=low+(high-low)//2
        
        if mid==arr[mid]:
            return mid
        elif arr[mid ]<mid:
            low=mid+1
        else:
            high=mid-1

    return -1

arr=[-10, -5, 0, 3, 7]
print(fixedpoint(arr))