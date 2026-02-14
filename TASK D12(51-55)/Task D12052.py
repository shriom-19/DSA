#Two Sum - Pair with given Sum
def hashset_method(arr, target):
    s=set()

    for i in range(len(arr)):

        key2=target-arr[i]

        if key2 in s:
            return True

        s.add(arr[i])
        
    return False

def two_pointer_method(arr,target):
    sorted(arr)

    i,j=0,len(arr)-1
    while i<j:
        total=arr[i]-arr[j]

        if (total < target):
            i+=1

        if (total == target):
            return True
        
        else:
            j-=1
        
    return False

arr = [1, -2, 1, 0, 5]
target = 0
print(hashset_method(arr,target))
print(two_pointer_method(arr,target))