#Maximum Consecutive Ones After Flipping Zeroes

def binary_one(arr,k):

    count1=0
    count0=0
    maxcount=0

    for i in range(len(arr)):
        
        if arr[0]==0:count0+=1

        if arr[i]==1 and count0<k:
            count1+=1

        if (arr[i]==0 and count0==k):
            count1=0
            count0=0
            
        maxcount=max(count1,maxcount)

    return maxcount+1

arr=[1, 0, 0, 1, 0, 1, 0, 1]
k = 2
print(binary_one(arr,k))

#correct approach
''' def maxOnes(arr, k):
    res = 0

    # Start and end pointer of the window
    start = 0
    end = 0

    # Counter to keep track of zeros in current window
    cnt = 0

    while end < len(arr):
        if arr[end] == 0:
            cnt += 1

        # Shrink the window from left if no. 
        # of zeroes are greater than k
        while cnt > k:
            if arr[start] == 0:
                cnt -= 1

            start += 1

        res = max(res, (end - start + 1))

        # Increment the end pointer 
        # to expand the window
        end += 1

    return res
'''