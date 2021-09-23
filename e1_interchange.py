"""
1.WAP to interchange 2nd and 4th elements in a list.
"""

l=list(input("Enter list elements\n").split())
print(l)
l[1],l[3]=l[3],l[1]
print(l)
