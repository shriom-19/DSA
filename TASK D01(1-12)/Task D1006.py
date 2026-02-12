addition=0

def sum_num(a:int):
    
    
    global addition
    addition += a%10

    if a//10<=0:
        return a
    
    return sum_num(a//10) 

n=int(input("enter the number to get addition of digit: "))

sum_num(n)

print(f"the sum of digits is :{addition}")


#easy approach
'''def sumOfDigits(n):
    # Base Case
    if n == 0:
        return 0
  
    # Recursive Case
    return n % 10 + sumOfDigits(n // 10)'''