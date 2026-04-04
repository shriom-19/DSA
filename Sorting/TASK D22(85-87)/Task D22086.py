#Minimum Platforms Required
def platforms(arr,dep):
    cnt=1
    i=1
    j=0
    arr.sort()  
    dep.sort()
    res=0
    while i <len(arr) and j <len(dep):
        
        if arr[i]<=dep[j]:
            cnt+=1
            i+=1
            
        else:
            cnt-=1
            j+=1
            
        res=max(cnt,res)
        
    return res

arr = [900, 940, 950, 1100, 1500, 1800]
dep = [910, 1200, 1120, 1130, 1900, 2000]
print(platforms(arr, dep))