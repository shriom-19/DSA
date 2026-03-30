from functools import cmp_to_key

def mycompare(s1,s2):
    if s1+s2> s2+s1:
        return -1
    else:
        return 1
    
def largest_num(arr):
    numbers=[str(ele) for ele in arr]
    
    numbers.sort (key=cmp_to_key(mycompare))
    
    if numbers[0]=="0":
        return "0"
    
    res="".join(numbers)
    
    return res

arr=[3, 30, 34, 5, 9]
print(largest_num(arr))