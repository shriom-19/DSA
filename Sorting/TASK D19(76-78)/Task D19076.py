#Merge Overlapping Intervals
def merge(arr):
    res=[]
    arr.sort()
    start=arr[0][0]
    end=arr[0][1]
    for i in range (1,len(arr)):
        
        if arr[i][0]< end:
            end=max(arr[i][1],end)
        elif arr[i][0] > end:
            res.append([start,end])
            start=arr[i][0]
            end=arr[i][1]
            
    res.append([start,end])
    return res

arr=[[7, 8], [1, 5], [2, 4], [4, 6]]
print(merge(arr))