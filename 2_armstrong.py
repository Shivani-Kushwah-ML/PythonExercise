"""
2.WAP to check whether the number is armstrong.
1, 2, 3, 4, 5, 6, 7, 8, 9, 153, 370, 371, 407, 1634, 8208,...
"""

def is_armstrong(num):
    cp=num
    temp=num
    count=0
    #Count number of digits in number
    while cp>0:
        cp//=10
        count+=1    
    #print(count)
        
    #logic for armstrong
    sum=0
    while temp > 0:
       digit = temp % 10
       sum += digit ** count
       temp //= 10
       
    return(bool(sum==num))
       
    
try:
    num = int(input("Please enter a number: "))
    if(is_armstrong(num)):
        print(num,end="")
        print(" is armstrong ")
    else:
        print(str(num) + " is not armstrong ")
except ValueError:
    print("Oops!  That was no valid number.  Try again...")
