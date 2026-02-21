#Rearrange array to make arr[i] = i

def rearange(arr):

    n=len(arr)
    i=0

    while i < n :
        if arr[i]!=-1 and arr[i]!=arr[arr[i]]:
            temp=arr[arr[i]]
            arr[arr[i]]=arr[i]
            arr[i]=temp

        else:
            i+=1

arr=[-1, -1, 6, 1, 9, 3, 2, -1, 4, -1]
rearange(arr)
print(arr)