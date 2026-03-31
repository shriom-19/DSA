#Meeting Rooms - Check if a person can attend all meetings

def canattend(arr):
    arr.sort()
    
    for i in range (len(arr)-1):
        if arr[i][1]>arr[i+1][0]:
            return False
    return True
    
    
def CanAttend(arr):
    n = len(arr)
    
    # Sort the meetings by their start times
    arr.sort(key=lambda x: x[0])
    
    for i in range(n - 1):
        
        # Compare the current meeting's end time with the 
        # next meeting's start time to check for overlap
        if arr[i][1] > arr[i + 1][0]:
            return False
    return True
arr= [[2, 4], [1, 2], [7, 8], [5, 6], [6, 8]]
print(canattend(arr))