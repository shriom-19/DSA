##highest GDC 
def gcd(a,b):
    return a if b==0 else gcd(b,a%b)

a=5
b=10
print(gcd(a,b))

# lowest common multiple
def LCM(a,b):
    return a*b/gcd(a,b)

print(f"LCM is: {LCM(a,b)}")