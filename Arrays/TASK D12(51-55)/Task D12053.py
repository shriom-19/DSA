#Split array into three equal sum segments

def findsegments(arr):
    total=sum(arr)
    if total%3!=0:
        return [-1,-1]
    
    target=total//3
    tempsum=0
    res=[]

    for i in range (len(arr)):
        tempsum+=arr[i]

        if target==tempsum:
            res.append(i)
            tempsum=0

    return res[:]

arr=[1, -1, 1, -1, 1, -1, 1, -1]
print(findsegments(arr))


