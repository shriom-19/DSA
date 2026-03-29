#Largest pair sum in an array

def maxpair(arr):

    if len(arr)<2:
        return -1
    max1=0
    max2=0
    for i in range(len(arr)):
        if max1<arr[i]:
            max2=max1
            max1=max(max1,arr[i])


    return max2+max1

arr = [12, 34, 10, 6, 40]
print("Max Pair Sum is", maxpair(arr))

