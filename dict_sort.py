"""
4.WAP to sort dictionary by key or value
"""

def by_key(d, reverse = False):
  return dict(sorted(d.items(), reverse = reverse))

s = {1:'app', 12:'bat', 4:'dot', 3:'cat' }
print("Sorted by key\n")
print(sorted(s.items()))
print("\n\nSorted by value\n")
sv=(sorted(s.items(), key=lambda x: x[1]))
print(sv)





'''
print("\nAscending order ")
print(by_key(s))
print("\nDescending order ")
print(by_key(s, True))
'''

'''
fruits={}
for i in range(2):
	key = input("Enter key for fruits:")
	value = input("Enter value for fruits:")
	fruits[key] = value
print(fruits)
'''
