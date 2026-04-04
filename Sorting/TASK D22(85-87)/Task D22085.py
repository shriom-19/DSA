#Intersection of Two Sorted Arrays

def merge(a,b):
    i=j=k=0
    res=[]
    
    while i<len(a) and j<len(b):
        
        if a[i-1]==a[i]:
            i+=1
            continue
        
        if a[i]==b[j]:
            res.append(a[i])
            i+=1
            j+=1
        
        
            
        if a[i]<b[j]:
            i+=1
            
        elif a[i]>b[j]:
            j+=1
            
    return res
            
a = [3, 5, 10, 10, 10, 15, 15, 20]
b = [5, 10, 10, 15, 30]
res = merge(a, b)
print(res)