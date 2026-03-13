def findMaximum(arr):
    n = len(arr)

    # Check if the first element is maximum
    if n == 1 or arr[0] > arr[1]:
        return arr[0]

    # Check if the last element is maximum
    if arr[n - 1] > arr[n - 2]:
        return arr[n - 1]

    # Search Space for binary Search
    lo, hi = 1, n - 2

    while lo <= hi:
        mid = lo + (hi - lo) // 2

        # If the element at mid is maximum then return it
        if arr[mid] > arr[mid - 1] and arr[mid] > arr[mid + 1]:
            return arr[mid]

        # If next element is greater, then maximum
        # element will exist in the right subarray
        if arr[mid] < arr[mid + 1]:
            lo = mid + 1

        # Otherwise, it will exist in left subarray
        else:
            hi = mid - 1

    return arr[hi]


arr = [1, 2, 4, 5, 7, 8, 3]
print(findMaximum(arr))