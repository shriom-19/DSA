#search Sencond large

def second_large(arr):
    n=len(arr)
    max1=arr[0]
    max2=0

    for i in range(1,n):
        if arr[i]>max1:
            max2=max1
            max1=arr[i]

        elif arr[i]> max2 and arr[i]<max1:
            max2=arr[i]
    
    return max2
        

arr = [12, 35, 1, 10, 34, 1]
print(second_large(arr))