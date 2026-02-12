def check_repeat( a, b ):
    
    if a%b==0:
        return a/b
    
    res=""
    rem=a%b
    mp = {}

    while ( rem > 0 and rem not in mp):

        mp[rem]= len(res)

        rem=rem*10

        res_part=rem// b 
        res+= str(res_part)

        rem=rem % b

    if (rem==0):
        return ""
    else:
        return res[mp[rem]:]


num,denum=22,7
res=check_repeat(num,denum)

print(res)