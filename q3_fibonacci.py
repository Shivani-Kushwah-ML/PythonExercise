"""
3.WAP to print fibonacci series using recursion between n1 and n2
(n1 and n2 should be user inputs)
"""
'''
def fibo(n):
    f,s=0,1
    
    
    return fibo(n-1) + fibo(n-2)
'''
import math
a = int(input('Enter a positive integer'))
z = int(input('Enter termination number'))

while a < z:
    a = a
    z = z
    b = ((5 * a * a) + 4)
    c = ((5 * a * a) - 4)
    d = math.sqrt(b)
    e = math.sqrt(c)


    if d % 1 == 0 or e % 1 == 0:
        print(str(a))
    a = a + 1




'''
def recur_fibo(n):  
   if n <= 1:  
       return n  
   else:  
       return(recur_fibo(n-1) + recur_fibo(n-2))  
 
nterms = int(input("How many terms? "))  
# check if the number of terms is valid  
if nterms <= 0:  
   print("enter positive integer")  
else:  
   print("series:")  
   for i in range(nterms):  
       print(recur_fibo(i))
'''
