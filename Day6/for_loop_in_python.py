"""FOR statement


The for statement in Python differs a bit from what you may be used to in C or Pascal.
Rather than always iterating over an arithmetic progression of numbers (like in Pascal), or
giving the user the ability to define both the iteration step and halting condition (as C),
Python`s for statement iterates over the items of any sequence (a list or a string), in the
order that they appear in the sequence. For example (no pun intended):
"""

"""FOR statement"""
alist=[1,2,3,5,6,7]
for x in alist:
    print(x**2)

blist=[]
for x in alist:

    blist.append(x**2)

print(alist)
print(blist)

clist=[]
for x in blist:
    y=x**2
    if y >100:
        clist.append(x**2)
print(clist)

# definite iteration
# run loop 5 times because list contains 5 items

alist=[5,7,9,45,67]

result=0
for i in alist:
    result+=i
    print(result)

print(result)

# definite iteration
# run loop 5 times because list contains 5 items

for i in range(10):
    print(i)
for i in range(10, 100):
    print(i)

for i in range(10, 100, 10):
    print(i)

astring="Today is beautiful"
bstring=""
 for i in range(len(astring)-1, -1, -1):
     #print(astring[i])
     bstring+=astring[i]

print(bstring)

"""BREAK statement"""
letters=" "

for i in astring:
    if i==" ":
        break
    else:
        print(i)

cstring=""
for i in astring:
    print(i)
    if i=="a":
        cstring += "x"
    else:
        cstring+=i
print(cstring)

#  enumerate() in a loop.

# When looping through a sequence, the position index and corresponding value can be retrieved
# at the same time using the enumerate() function

astring="Python is a great language"
index_list=[]
char_list=[]
for index, char in enumerate(astring):
    if char in ("a","e","o" ,"u","i"):
        index_list.append(index)
        char_list.append(char)
print (index_list, char_list)


# To loop over two or more sequences at the same time, the entries can be paired with
# the zip() function.

names=["james","Kevin","Hasan"]
lastname=["Smith","white","raman"]
ages=[23,67,19]
adict={}
for name, lname, age in zip(names, lastname, ages):
    print(f"Hi! My name is {n}. My last name is {ln}, I am {age} years old")
    adict["name"]=name
    adict["lastname"] = lname
    adict["age"]=age
print(adict)


