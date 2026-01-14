# file I/O operations
"""f = open("seven.txt", "r")
data = f.read()
 
f = open("seven.txt", "a")
data = f.write("\nI live in Gadhsisa")
print(data)

a = f.write("\nI am now in Dubai")
print(data)
print(a)

with open("seven.txt", "a") as f:
    data = f.write("\nyou are my best friend")
    print(data)
f.close()

with open("ten.txt", "w") as f:
   data = f.write("Hi, Everyone,\nWe are learning file I/O here\nUsing java.\nI like programming in java")
    #print(data)
with open("ten.txt", "r") as f:
  data = f.read()
  a = data.replace("java","Python")
  print(a)

  with open("ten.txt", "w") as f:
     f.write(a)"""

a = "file"
with open("ten.txt","r") as f:
    data = f.read()
    if(data.find(a) != -1) :
       print("Data Found")
    else :
        print("Not Found")
     