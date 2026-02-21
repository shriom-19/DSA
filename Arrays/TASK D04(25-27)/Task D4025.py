#powersets

def powerset(a):
    subset=[]
    n=len(a)
    for i in range(1<<n):

        temp=""
        for j in range (n):

            if i & (1<<j):
                temp=temp+a[j]
        subset.append(temp)

    return subset


str1="abc"
for set in powerset(str1):
    print(set)
    