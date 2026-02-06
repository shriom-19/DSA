#Leaders in an array

def find_leader(arr):
    maxelement=arr[-1]
    n=len(arr)
    res=[]

    for i in range( n-1, -1, -1 ):
        if (arr[i] >= maxelement):
            maxelement = arr[i]
            res.append(maxelement)

    res.reverse()
    return res
arr = [1, 2, 3, 4, 5, 2]
print (find_leader(arr))