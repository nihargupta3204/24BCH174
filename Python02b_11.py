#Given three points (x1,y1), (x2,y2) and (x3,y3), check if all the three points fall on one straight 
#line.
x1 = int(input("Enter first abbssica"))
x2 = int(input("Enter second abbssica"))
x3 = int(input("Enter third abbssica"))
y1 = int(input("Enter first ordinate"))
y2 = int(input("Enter second ordinate"))
y3 = int(input("Enter third ordinate"))
slope1 = (y2 - y1) * (x3 - x1)
slope2 = (y3 - y1) * (x2 - x1)
if (slope1 == slope2):
    print("line is coinsident")
else:
    print("not coinsident")