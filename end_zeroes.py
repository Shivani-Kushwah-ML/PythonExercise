"""
2.Write a Python program to find the number of zeros at the end of a factorial
of a given positive number.
"""
n=int(input("enter a number "))
f=1
if n==0:
    print(0)
else:
    for i in range(1,n+1):
        f*=i

    i=5
    cnt=0
    while (n/i>=1):
        cnt += n//i
        i*=5
    print(cnt)
# factors continuosly divide by primes then (2*5) power of 5
