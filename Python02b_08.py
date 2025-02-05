#Check whether a triangle is valid or not, when the three angles of the triangle are entered 
a1 = int(input("Enter first angle for triangle"))
a2 = int(input("Enter second angle for triangle"))
a3 = int(input("Enter third angle for triangle"))
a4 = a1 + a2 + a3
if (a4 == 180):
    print("Entered angles are valid")
else:
    print("Entered angles are not valid")