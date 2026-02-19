#K-th Largest Sum Contiguous Subarray
import heapq

def kth_largest(arr,k):
    
    
    n=len(arr)
    prefix=[0]*(n+1)


    for i in range(1,n+1):
        prefix[i]=prefix[i-1]+arr[i-1]


    subarry=[]
    heapq.heapify(subarry)

    for i in range(n+1):

        for j in range (i+1, n+1):
            subarrysum=prefix[j]-prefix[i]
            if len(subarry)<k:
                heapq.heappush(subarry,subarrysum)
            else:
                if subarrysum>subarry[0]:
                    heapq.heapreplace(subarry,subarrysum)



    return subarry[0]

arr =[20, -5, -1]
k = 3
print(kth_largest(arr, k))