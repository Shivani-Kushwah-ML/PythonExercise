'''
4.Write a Python program to reverse the digits of a given number and add it to
the original, If the sum is not a palindrome repeat this procedure.
(Take range between 100 to 10000)
'''

n=(input("Enter 1 no. between 100 to 10000"))
sm=n
o=n
while True:
    rev=int(str(sm)[::-1])
    sm= int(n)+rev
    n=sm
    if( sm == int(str(sm)[::-1])):
        print(sm)
        break
    
       

