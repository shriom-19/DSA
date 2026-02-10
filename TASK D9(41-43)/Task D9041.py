#Minimum cost to make array size 1 by removing larger of pairs
def minimun_cost(arr, n):
    if n<=1:
        return 0
    
    arr[0]=min(arr[0],arr[n-1])
    res=arr[0]
    del arr[n-1]
    
    return res + int(minimun_cost(arr,len(arr)))
    

arr=[4 ,3 ,2 ]
print(minimun_cost(arr, len(arr)))



#easy logic
""" def cost(a, n):

    # Minimum cost is n-1 multiplied
    # with minimum element.
    return ( (n - 1) * min(a) )


# driver code
a = [ 4, 3, 2 ]
n = len(a)
print(cost(a, n))"""