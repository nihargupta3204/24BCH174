def find_largest_smallest(a,b,c):
    largest = max(a,b,c)
    smallest = min(a,b,c)
    return largest,smallest
i1 = 4
i2= 3
i3 = 9
largest, smallest = find_largest_smallest(i1,i2,i3)
print("The largest number is {largest}")
print("The smallest number is {smallest}")

