#Kth smallest element in a row-wise and column-wise sorted 2D array

import heapq

def kthmatrix(mat,k):
    n=len(mat)

    hq=[]

    for i in range(n):
        for j in range(n):
            current=mat[i][j]
            heapq.heappush(hq,-current)

            if len(hq)>k :
                heapq.heappop(hq)


    return -hq[0]


mat = [[10, 20, 30, 40],
       [15, 25, 35, 45],
       [24, 29, 37, 48],
       [32, 33, 39, 50]]
k = 3

print(kthmatrix(mat,k))


