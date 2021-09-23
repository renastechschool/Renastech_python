## PYTHON DATA TYPES: LIST ###
"""Lists.
Python knows a number of compound data types, used to group together
other values. The most versatile is the list, which can be written as a
list of comma-separated values (items) between square brackets. Lists
might contain items of different types, but usually the items all have
the same type.
"""

# Lists are very similar to arrays. They can contain any type of variable, and they can contain
# as many variables as you wish. Lists can also be iterated over in a very simple manner.
# Here is an example of how to build a list.

alist=[1,2,4,5,6,7,45]
print(type(alist))

print(alist[0])
print(alist[-1])
print(alist[-3])
print(alist[1:5])

# Lists also support operations like concatenation:
blist=alist+[77,88,99]
print(blist)

# Unlike strings, which are immutable, lists are a mutable type, i.e. it
# is possible to change their content:
blist[5]="hello"
print(blist)

# You can also add new items at the end of the list, by using
# the append() method
blist.append(216)
print(blist)

# Assignment to slices is also possible, and this can even change the size
# of the list or clear it entirely:
blist[6:9]=["a","b","c"]
print(blist)

# clear the list by replacing all the elements with an empty list
#blist[:]=[]
print(blist)

# The built-in function len() also applies to lists
print(len(blist))

# It is possible to nest lists (create lists containing other lists),
# for example:
clist=[1,2,3]
dlist=["a","b","c"]
merge_list=clist+dlist
print(merge_list)

merge_list=[clist,dlist]
print(merge_list)

print(merge_list[0][1])

# methods for list

# list.append(x)
# Add an item to the end of the list.
fruits = ['orange', 'apple', 'pear', 'banana', 'kiwi', 'apple', 'banana']
fruits.append("grape")
print(fruits)

# list.remove(x)
# Remove the first item from the list whose value is equal to x.
# It raises a ValueError if there is no such item.
 fruits.remove("grape")
print(fruits)

# list.insert(i, x)
# Insert an item at a given position. The first argument is the index of the element
# before which to insert, so a.insert(0, x) inserts at the front of the list,
# and a.insert(len(a), x) is equivalent to a.append(x).
fruits.insert(1, "grabe")
fruits.insert(2, "grabe")
print(fruits)

# list.count(x)
# Return the number of times x appears in the list.
print(fruits.count("grabe"))


# list.reverse()
# Reverse the elements of the list in place.
fruits.reverse()
print(fruits)

# list.pop([i])
# Remove the item at the given position in the list, and return it. If no index is specified,
# a.pop() removes and returns the last item in the list. (The square brackets around the i in
# the method signature denote that the parameter is optional, not that you should type square
# brackets at that position.)

fruits.pop(5)
print(fruits)



"""The del statement

There is a way to remove an item from a list given its index instead of its value: the del
statement. This differs from the pop() method which returns a value. The del statement can also
be used to remove slices from a list or clear the entire list (which we did earlier by
assignment of an empty list to the slice).
"""
del fruits[2]
print(fruits)

del fruits
print(fruits)

"""List Comprehensions.

List comprehensions provide a concise way to create lists. Common applications are to make new
lists where each element is the result of some operations applied to each member of another
sequence or iterable, or to create a subsequence of those elements that satisfy a certain
condition.

A list comprehension consists of brackets containing an expression followed by a for clause,
then zero or more for or if clauses. The result will be a new list resulting from evaluating
the expression in the context of the for and if clauses which follow it.
"""

alist=[1,2,3,4,5,6,7,8,9]
for i in alist:
 print(i)

blist=[]
for i in alist:
  if i > 5:
   blist.append(i)
print(blist)

blist=[i for i in alist if i>5]
print(blist)

clist=[i**2 for i in alist]
print(clist)

import math
dlist=[math.sqrt(i) for i in alist]
print(dlist)