def swap_count(arr):
    n = len(arr)
    swaps = 0
    
    temp = sorted(arr)
    
    # value -> index mapping
    pos = {}
    for i in range(n):
        pos[arr[i]] = i   # map current positions
    
    i = 0
    while i < n:
        correct_value = temp[i]
        
        # if current element is not correct
        if arr[i] != correct_value:
            swaps += 1
            
            # index where correct value is present
            to_swap_idx = pos[correct_value]
            
            # update hashmap BEFORE swap
            pos[arr[i]] = to_swap_idx
            
            # swap
            arr[i], arr[to_swap_idx] = arr[to_swap_idx], arr[i]
            
            # update hashmap AFTER swap
            pos[correct_value] = i
        else:
            i += 1
    
    return swaps


arr = [2, 8, 5, 4]
print(swap_count(arr))