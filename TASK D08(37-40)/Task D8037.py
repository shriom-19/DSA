#Program to find number of squares in a chessboard

def CountSquare(n):
    if n == 1:
        return 1
    return (n*n)+CountSquare(n-1)

def distinctRectangles(n):
    ans = 0;
    ans = (n * (n + 1)) / 2;
    return int(ans);

n =8

print (f"number of squares: {CountSquare(n)}")

print (f"number of squares: {distinctRectangles(n)}")