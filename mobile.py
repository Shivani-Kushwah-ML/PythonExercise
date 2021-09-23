'''
3.Write a Python program to find the digits which are absent in a given mobile number.
'''
digits=set([1,2,3,4,5,6,7,8,9,0])
mob= input("Enter mobile num \n")
x= set([int(a) for a in str(mob)])
#set difference
print(digits-x)
