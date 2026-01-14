#List and Tuple
"""name=["karan",90.5,18,"Gujarat"]
print(name)
print(name[1:3])
print(name[-3:-1])
value=[1,2,5,8,6]
print(value)
print(value.append(4))
print(value.sort(reverse=True))
print(value)
value=['a','b','e','c','d','f']
print(value.reverse())
print(value.insert(2,'g'))
print(value.remove('a'))
print(value.pop(2))
print(value)
value=(1,2,3,1,4,5,1)
print(type(value))
print(value.index(2))
print(value.count(1))"""
value = ["r","a","c","e","c","a","r"]
a = value.copy()
a.reverse()
if(a == value):
    {
        print("Palindrome")
    }
else:
    {
        print("is not a palindrome")
    }

    #print(value)