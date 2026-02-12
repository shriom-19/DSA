#Rearrange array such that even positioned are greater than odd

def rearange(arr):
    n=len(arr)

    for i in range(1,n):
        if ((i+1)%2==0):
            if (arr[i]<arr[i-1]):
                arr[i],arr[i-1]=arr[i-1],arr[i]

        else:
            if (arr[i]>arr[i-1]):
                arr[i],arr[i-1]=arr[i-1],arr[i]

    return  arr



arr=[1, 2, 3, 4, 5, 6]

print(rearange(arr))