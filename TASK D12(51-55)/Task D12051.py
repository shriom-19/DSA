#Equilibrium Index 

def equilibrium(arr):
    total=sum(arr)
    prefix=0
    

    for i in range(len(arr)):
        
        suffix=total-prefix-arr[i]

        if prefix==suffix:
            return i
            
        prefix+=arr[i]

    return -1

arr = [1, 7, 3, 6, 5, 6]

print(equilibrium(arr))

