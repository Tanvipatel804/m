#Function and Recursion

"""letter = ["apple","ball","cat","dog","Elephant"]
def list_length(letter):
       print(letter)
       print(len(letter))
       for items in letter :
        print(items,end="$")
       return

list_length(letter)     #Function

def fact(n) :
    fact=1
    for i in range(1, n+1) :
        fact *= i
        print(fact)

fact(5)

no = int(input("Enter any no : "))
def odd_even(no) :
    if(no % 2 == 0):
        print(no, "is even number")
    else :
        print(no, "is odd no")
    return

odd_even(no)"""

n = int(input("Enter any no : ")) #Recursion
def fact(n):
    if(n == 1 or n ==0):
        return 1
    else :
        return n * fact(n-1)
a=fact(n)
print(a)