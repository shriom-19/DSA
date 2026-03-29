#Sort an array of strings according to string lengths
def merge(arr,left,mid,right):
    L=arr[left:mid+1]
    R=arr[mid+1:right+1]
    
    i=j=0
    k=left
    
    while i<len(L) and j<len(R):
        if len(L[i]) <= len(R[j]):
            arr[k]=L[i]
            i+=1
            
        else:
            arr[k]=R[j]
            j+=1
        k+=1
        
    while i < len(L):
        arr[k] = L[i]
        i += 1
        k += 1
        
    while j < len(R):
        arr[k] = R[j]
        j += 1
        k += 1
    


def mergesort(arr,left,right):
    if  left < right:
        mid=left+(right-left)//2
        mergesort(arr,left,mid)
        mergesort(arr,mid+1,right)
        merge(arr,left ,mid,right )
    


def sortwords(arr):
    mergesort(arr,0,len(arr)-1)
    
arr=["GeeksforGeeks", "I", "from", "am"]
sortwords(arr)
print(arr)
    