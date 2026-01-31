a=list([])
for i in range (2):
    a.append(int(input("enter num:")))

n=int(input("enter n(count): "))
#formula
nth=a[0]+(n-1)*(a[1]-a[0])

print(f"nth term is : {nth}")