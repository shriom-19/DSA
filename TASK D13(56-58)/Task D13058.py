#Product of Array Except Self

def product_arr(arr):
    zeros=0
    product=1
    index=0

    for i in range(len(arr)):
        if arr[i]==0:
            zeros+=1
            index=i

        else:
            product*=arr[i]

    if zeros>1:
        return [0]*len(arr)
    
    if zeros==1:
        res=[0]*len(arr)
        res[index]=product
        return res
    else:
        for i in range(len (arr)):
            arr[i]=product//arr[i]

    return arr

arr = [12, 0]

print(product_arr(arr))