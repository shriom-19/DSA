#Find the Missing 

def natrual_sum_approach(arr):

    n=len(arr)+1

    totalsum=sum(arr)

    actualsum=n*(n+1)//2

    return actualsum-totalsum

def xor_method(arr):
    n=len(arr)+1

    xor1=0
    xor2=0

    for i in range(n-1):
        xor1^=arr[i]

    for i in range(1,n+1):
        xor2^=i

    return xor1 ^ xor2

arr=[8, 2, 4, 5, 3, 7, 1]

print(natrual_sum_approach(arr))
print(xor_method(arr))