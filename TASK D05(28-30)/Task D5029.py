#Tower of Hanoi

def towerofhanoi(n , fromrod, torod, extrarod):
    if n== 0:
        return 
    towerofhanoi(n-1,  fromrod , extrarod ,torod )

    print(f" Disk {n} moved from {fromrod} to {torod}")

    towerofhanoi(n-1 ,extrarod , torod , fromrod  )

n=6
towerofhanoi(n,"A","C","B")