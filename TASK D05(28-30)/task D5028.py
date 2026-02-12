# Angle betwwen Clock
def findangle( a , b):

    a=a%12

    Hr=30*a+0.5*b

    mi=6*b

    angle=(Hr-mi)

    return (Hr-mi)


str1=input(" Enter time into format [HH:MM] :-  ")
h=int(str1[:2])
m=int(str1[3:])
print(findangle(h,m))
