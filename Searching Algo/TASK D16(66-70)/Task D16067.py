#Find common elements in three sorted arrays
def binary_search(arr,n,m):
    l=0
    h=n-1

    while l<=h:
        mid=l+(h-l)//2

        if arr[mid]==m:
            return arr[mid]

        elif arr[mid]<m:
            l=mid+1

        else:
            h=mid-1
    
    return -1
    


def common_three(arr1,arr2,arr3):
    
    n1=len(arr1)
    n2=len(arr2)
    n3=len(arr3)

    if n1<n2 and n1<n3:
        arr=arr1
    if n2<n1 and n2<n3:
        arr=arr2
    else:
        arr=arr3

    res=[]
    for i in arr:
        if (binary_search(arr1,n1,i) and binary_search(arr2,n2,i) and binary_search(arr3,n3,i)):
            res.append(i)

    return res

arr1 = [1, 5, 10, 20, 30]
arr2 = [5, 13, 15, 20]
arr3 = [5, 20]

print(common_three(arr1,arr2,arr3))

def commonElements(arr1, arr2, arr3):
    i, j, k = 0, 0, 0
    common = []

    while i < len(arr1) and j < len(arr2) and k < len(arr3):
        if arr1[i] == arr2[j] == arr3[k]:
            common.append(arr1[i])
            i += 1
            j += 1
            k += 1

            while i < len(arr1) and arr1[i] == arr1[i - 1]:
                i += 1
            while j < len(arr2) and arr2[j] == arr2[j - 1]:
                j += 1
            while k < len(arr3) and arr3[k] == arr3[k - 1]:
                k += 1

        elif arr1[i] < arr2[j]:
            i += 1
        elif arr2[j] < arr3[k]:
            j += 1
        else:
            k += 1

    return common

print(commonElements(arr1,arr2,arr3))