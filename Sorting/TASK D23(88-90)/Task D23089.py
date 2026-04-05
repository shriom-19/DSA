def merge(arr, left, mid, right, res):
    temp = []
    i, j = left, mid + 1
    
    # count how many elements from right are greater
    right_count = 0
    
    while i <= mid and j <= right:
        if arr[i][0] < arr[j][0]:
            # all remaining right elements are greater
            res[arr[i][1]] += (right - j + 1)
            temp.append(arr[i])
            i += 1
        else:
            temp.append(arr[j])
            j += 1
    
    while i <= mid:
        temp.append(arr[i])
        i += 1
    
    while j <= right:
        temp.append(arr[j])
        j += 1
    
    # copy back
    for i in range(len(temp)):
        arr[left + i] = temp[i]


def countmerge(arr, left, right, res):
    if left >= right:
        return
    
    mid = (left + right) // 2
    
    countmerge(arr, left, mid, res)
    countmerge(arr, mid + 1, right, res)
    
    merge(arr, left, mid, right, res)


def surpasser_count(arr):
    n = len(arr)
    
    # store (value, original_index)
    arr_with_index = [(arr[i], i) for i in range(n)]
    
    res = [0] * n
    
    countmerge(arr_with_index, 0, n - 1, res)
    
    return res


arr = [2, 7, 5, 3, 8, 1]
print(surpasser_count(arr))