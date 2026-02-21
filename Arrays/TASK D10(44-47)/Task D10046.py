#Unique Number I

def find_once(arr):
    temp=dict()
    for i in arr:
        if i in temp:
            temp[i]+=1
        else:
            temp[i]=1

    for i,j in temp.items():
        if j==1:
            return i
        
arr=[2, 2, 5, 5, 20, 30, 30]
print(find_once(arr))


"""def findUnique(arr):
    res = 0
    
    # Find XOR of all elements
    for num in arr:
        res ^= num
    
    return res"""
