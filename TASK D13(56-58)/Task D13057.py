#Reorder an array according to given indexes
def rearange(arr,index):
    n=len(arr)

    if len(arr)!=len(arr):
        return -1
    
    for i in range ( n ):
        while(index[i]!=i):
            temp=arr[index[i]]
            tempin=index[index[i]]
            arr[index[i]]=arr[i]
            index[index[i]]=index[i]
            arr[i]=temp
            index[i]=tempin

    return arr

arr= [50, 40, 70, 60, 90]
index= [3,  0,  4,  1,  2]
print(rearange(arr,index))





#deadly (easy) Aproach

'''# Python program to reorder arr[] using index[]
# using Mathematical Encoding 

def reorderArray(arr, index):

    n = len(arr)

    # Find the maximum value
    maxVal = arr[0]
    for i in range(1, n):
        if arr[i] > maxVal:
            maxVal = arr[i]

    # Set value as max + 1
    value = maxVal + 1

    # Encode both old and new 
    # values at index[i]
    for i in range(n):
        arr[index[i]] += (arr[i] % value) * value

    # Decode to get the reordered values
    for i in range(n):
        arr[i] = arr[i] // value

# Driver code
if __name__ == "__main__":

    arr = [10, 11, 12]
    index = [1, 0, 2]

    reorderArray(arr, index)

    # Print the updated array
    for i in range(len(arr)):
        print(arr[i], end=' ')'''
