#sort in specific order

def specific(arr):
    n=len(arr)
    i=0
    j=len(arr)-1
    
    while i <= j:
        if arr[i]%2==1:
            i+=1
        else:
            arr[i],arr[j]=arr[j],arr[i]
            j-=1
            
    arr[:i]=sorted(arr[:i],reverse=True)
    arr[i:]=sorted(arr[i:])
    
    
            
arr=[0,1,2,3,4,5,6,7,8,9] 
specific(arr)
print(arr)