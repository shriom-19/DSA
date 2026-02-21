#Find k largest elements in an array
import heapq


def k_largest(arr,k):
    maxheap=[n for n in arr]
    heapq.heapify(maxheap)

    return heapq.nlargest(3, maxheap)

arr=[1, 23, 12, 9, 30, 2, 50]
k=3
print(k_largest(arr,k))
