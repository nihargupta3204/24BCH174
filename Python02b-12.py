# Given the coordinates (x,y) of center of a circle and its radius, determine whether a point lies 
#inside the circle, on the circle or outside the circle. (Hint: Use sqrt( ), pow( ) ) 
import math
cx, cy = map(int, input("Enter the coordinates of the center of the circle (cx cy): ").split())
r = float(input("Enter the radius of the circle: "))
px, py = map(int, input("Enter the coordinates of the point (px py): ").split())
distance = math.sqrt(pow(px - cx, 2) + pow(py - cy, 2))
if distance < r:
    print("The point lies inside the circle.")
elif distance == r:
    print("The point lies on the circle.")
else:
    print("The point lies outside the circle.")
