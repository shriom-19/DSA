#Sorted subsequence of size 3

def sorted3(arr):

    result=[]
    track=0

    for i in range(len (arr)-1):
        if arr[i]<arr[i-1] and arr[i]<arr[i+1]:
            result.append(arr[i])
            track=i
            break

    for i in range(track ,len(arr)):
        if arr[i]>result[-1]:
            result.append(arr[i])

    return result[:3]

arr=[4, 3, 2, 1]
print(sorted3(arr))

#broken logic above


# corrected logic
## https://www.geeksforgeeks.org/dsa/find-a-sorted-subsequence-of-size-3-in-linear-time/