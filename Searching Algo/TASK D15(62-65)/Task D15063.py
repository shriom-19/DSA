def find_repeat(arr):
    
    unique=set([])

    infite=float('inf')

    for i in range(len(arr)-1,-1,-1):
        if arr[i] in unique:
            infite=min(infite,i)
        unique.add(arr[i])

    return -1 if infite==float('inf') else arr[infite]

arr= [6, 10, 5, 4, 9, 120, 4, 6, 10]
print(find_repeat(arr))