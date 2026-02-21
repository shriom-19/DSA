#Stock Buy and Sell - Multiple Transaction 
def max_profit(arr):
    profit=0

    for i in range(len(arr)-1):
        if arr[i]>arr[i+1]:
            pass
        else:
            profit+=arr[i+1]-arr[i]
    
    return profit

arr= [100, 180, 260, 310, 40, 535, 695]
#arr=[4, 2]
print(max_profit(arr))
        
