#Duplicate within K Distance in an Array

def duplicate_within(arr,k):
    n=len(arr)

    for i in range(n-k):
        if len(set(arr[i:i+k+1]))<=k:
            return "yes"
        
    return "no"

arr=[10, 5, 3, 4, 3, 5, 6]
k=3
print(duplicate_within(arr,k))


#optimized solution

""" def duplicate_within(arr, k):
    seen = set()

    for i in range(len(arr)):
        if arr[i] in seen:
            return "yes"

        seen.add(arr[i])

        if i >= k:
            seen.remove(arr[i - k])

    return "no" """