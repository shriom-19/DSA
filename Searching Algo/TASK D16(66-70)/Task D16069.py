'''Given Array of size n and a number k, find all elements that appear more than n/k times
Last Updated : 23 Jul, 2025
Given an array of size n and an integer k, find all elements in the array that appear more than n/k times. 

Examples:

Input: arr[ ] = [3, 4, 2, 2, 1, 2, 3, 3], k = 4
Output: [2, 3]
Explanation: Here n/k is 8/4 = 2, therefore 2 appears 3 times in the array that is greater than 2 and 3 appears 3 times in the array that is greater than 2

Input: arr[ ] = [9, 10, 7, 9, 2, 9, 10], k = 3
Output: [9]
Explanation: Here n/k is 7/3 = 2, therefore 9 appears 3 times in the array that is greater than 2.'''



def morethanNbyK(arr, k):
    n = len(arr)
    x = n // k

   
    freq = {}

    for num in arr:
        freq[num] = freq.get(num, 0) + 1

   
    sorted_keys = sorted(freq.keys())

    
    for key in sorted_keys:
        
        if freq[key] > x:
        
            print(key)


arr = [3, 4, 2, 2, 1, 2, 3, 3]
k = 4
morethanNbyK(arr, k)


    