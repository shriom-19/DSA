#Maximum number of 2x2 squares that can be fit inside a right isosceles triangle
def fitsquare(base):
    base=(base-2)
    base=base//2
    return base * (base + 1) / 2

print(fitsquare(8))