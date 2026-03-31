#Minimize the moves required to seat each passenger in a chair
def cahir_passenger(chair,passenger):
    chair.sort()
    passenger.sort()
    ans=0
    for i in range(len(chair)):
        ans+=abs(chair[i]-passenger[i])
                
    return ans

chairs = [2, 2, 6, 6]
passengers = [1, 3, 2, 6]
print(cahir_passenger(chairs,passengers))