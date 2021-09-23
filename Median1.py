a=int(input("Enter 1st no. "))
b=int(input("Enter 2nd no. "))
c=int(input("Enter 3rd no. "))

if a > b:
    if a < c:
        median = a
    elif b > c:
        median = b
    else:
        median = c
else:
    if a > c:
        median = a
    elif b < c:
        median = b
    else:
        median = c

print("The median is", median)
