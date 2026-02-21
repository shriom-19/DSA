#Digital root 

def digitalsum(n):

    if len(n)<=1:
        return n
    sum=0
    for i in n:
        sum+=int(i)

    return digitalsum(str(sum))

num = input(" Enter a number: ")
print(type(num))

print(f"digital root of {num} is = {digitalsum(str(num))}")
    