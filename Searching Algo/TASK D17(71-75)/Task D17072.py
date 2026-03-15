#K’th Smallest Element
import heapq
def smallest_kelement(arr,k):
    hq=[]*k

    heapq.heapify(hq)
    i=0
    n=len(arr)

    while i<n:

        

        heapq.heappush(hq,-arr[i])
        if len(hq)>k:
            heapq.heappop(hq)
        i+=1

    

    return -heapq.heappop(hq)
    
arr=[10, 5, 4, 3, 48, 6, 2, 33, 53, 10]
k=4
print(smallest_kelement(arr,k))