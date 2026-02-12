# Rat and Poison

import math

def findRatno( bottles ):
    rats = math.log(bottles ,2)
    return math.floor(rats)

print(f"Rats required = {findRatno(16)}")