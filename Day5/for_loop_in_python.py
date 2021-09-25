"""FOR statement


The for statement in Python differs a bit from what you may be used to in C or Pascal.
Rather than always iterating over an arithmetic progression of numbers (like in Pascal), or
giving the user the ability to define both the iteration step and halting condition (as C),
Python`s for statement iterates over the items of any sequence (a list or a string), in the
order that they appear in the sequence. For example (no pun intended):
"""

"""FOR statement"""

# == use cases of for loops== #
# itarate trought items in a collection object(list, string, sets)
astring="Today is friday"
count=0
for i in astring:
    print (i)
    count+=1
print(count)
# update items in a iterable object

result=""
for k in astring:
    if k=="a":
        result+="X"
    elif k=="i":
        result+="Y"
    elif k=="o":
        result+="Z"
    else:
        result+=k
print (result)

blist=[1,2,3,4,5,6,7,9]
alist=[]
for i in blist:
    if i==1:
        alist.append(i*10)
    elif i==2:
        alist.append(i*20)
    elif i==3:
        alist.append(i*30)
    elif i==4:
        alist.append(i*40)
    elif i==5:
        alist.append(i*50)
    else:
        alist.append(i*100)
print (alist)
# subset an iterable object

subset_alist=[]
for i in alist:
    if i >=500:
        subset_alist.append(i)
print(subset_alist)
# iterate with range() method

for i in range(len(alist)):
    if alist[i] >=500:
        alist[i]=alist[i]*1000
    else:
       pass #alist.pop(i)
print(alist)

for i in range(i==0, i<=100, i+10):
    print (i)
# break statement in for loop

# continue statement in for loop

#  enumerate() method in a loop.
# When looping through a sequence, the position index and corresponding value can be retrieved
# at the same time using the enumerate() function

#  zip() method in a loop.
# To loop over two or more sequences at the same time, the entries can be paired with
# the zip() function.