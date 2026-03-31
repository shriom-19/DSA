#Tywin's War Strategy
import heapq

def tywin(arr,k):
    n=len(arr)
    need=n//2
    hpq=[]
    heapq.heapify(hpq)
    lucky=0
    
    for i in range(n):
        if arr[i] % k == 0:
            lucky+=1
        else:
            heapq.heappush(hpq,k-(arr[i]%k))
            
    if lucky >= need:
        return 0
    print(hpq)
    return sum(hpq[:need-lucky])

arr = [3, 5, 6, 7, 9, 11]
k = 4
print(tywin(arr,k))