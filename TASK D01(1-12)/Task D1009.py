# Input format: x1 y1 x2 y2
l1 = list(map(int, input("Enter L1 and R1 (x1 y1 x2 y2): ").split()))
l2 = list(map(int, input("Enter L2 and R2 (x1 y1 x2 y2): ").split()))

# Rectangle 1
x1_l, y1_l, x1_r, y1_r = l1

# Rectangle 2
x2_l, y2_l, x2_r, y2_r = l2

# Check overlap
if (x1_r <= x2_l or x2_r <= x1_l or
    y1_r >= y2_l or y2_r >= y1_l):
    print("Rectangles Don't Overlap")
else:
    print("Rectangles Overlap")
