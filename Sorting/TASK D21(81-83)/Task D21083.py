def union(arr1,arr2):
    
    
    i=j=k=0
    a=len(arr1)
    b=len(arr2)
    res=[]

    while i<a & j<b:
        if i > 0 and arr1[i-1]==arr1[i]:
            i+=1
            continue
        
        if arr2[j-1]==arr2[j] and j>0:
            j+=1
            continue
        
        if arr1[i]<arr2[j]:
            res.append(arr1[i])
            i+=1
            
        elif arr1[i]>arr2[j]:
            res.append(arr2[j])
            j+=1
                 
        
        else:
            res.push(arr1[i])
            i+=1
            j+=1
            
            
    while i<a:
        if i>0 and arr1[i-1]==arr1[i]:
            i+=1
            continue
        res.append(arr1[i])
        i+=1
            
    while j<b:
        if j>0 and arr2[j-1]==arr2[j]:
            j+=1
            continue
        res.append(arr2[j])
        j+=1
            
    return res

a = [1, 1, 2, 2, 2, 4]
b = [2, 2, 4, 4]
print(union(a,b))