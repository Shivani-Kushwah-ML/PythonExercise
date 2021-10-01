'''
5.Write a Python program to create all possible strings by
using 'a', 'e', 'i', 'o', 'u'. Use the characters exactly once.
'''

from itertools import permutations
l=['a','e','i','o','u']

p = permutations(l)
for i in list(p):
    print (i)
