#Sum Of All subarry

def subarry_sum(arr, i , j):
    if i==j:
        return arr[j]
    
    res=0
    for a in range(i,j+1):
        res+=sum(arr[i:a+1])

    return res+subarry_sum(arr,i+1,j)


arr=[1, 2, 3, 4]
print(arr[1:2])
n=len(arr)
print(subarry_sum(arr,0,n-1))