#cyclic sort 

def cyclic_sort(arr):
    n = len(arr)
    i = 0
    while i < n:
        correct = arr[i] - 1
        if arr[i] != arr[correct]:
            arr[i], arr[correct] = arr[correct], arr[i]
        else:
            i += 1

arr=[1, 8, 3, 9, 10, 10, 2, 4 ]
n = len(arr)
print("Before sorting array:")
print(arr)

# Function Call
cyclic_sort(arr)
print("Sorted array:")
print(arr)