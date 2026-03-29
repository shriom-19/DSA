#Sort an array in wave form

def Inwavearr(arr):
    
    n=len(arr)
    
    for i in range(1,n-1,2):
        if arr[i]>arr[i-1]:
            arr[i],arr[i-1]=arr[i-1],arr[i]
            
            
            
arr=[1,2,3,4,5]
Inwavearr(arr)
print(arr)