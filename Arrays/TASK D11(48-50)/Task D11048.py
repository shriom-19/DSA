#missing And repeting


def miss_repeat(arr):
    n=len(arr)

    xor1=0
    xor2=0

    result=[]

    for i in range(n-1):

        xor1^=arr[i]

    for i in range (1,n+1):
        xor2^=i

    result.append(xor1^xor2)

    arr.append(xor1^xor2)

    xor1=0

    for i in range(n+1):

        xor1^=arr[i]

    result.append(xor1^xor2)

    return result

arr=[3, 1, 3]
res=miss_repeat(arr)
print(f"missing num = {res[0]} and repeating num = {res[1]}")


        