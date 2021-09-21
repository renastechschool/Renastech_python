# ### PYTHON DATA TYPES: LIST ###
# """Lists.
# Python knows a number of compound data types, used to group together
# other values. The most versatile is the list, which can be written as a
# list of comma-separated values (items) between square brackets. Lists
# might contain items of different types, but usually the items all have
# the same type.
# """
#
# # Lists are very similar to arrays. They can contain any type of variable, and they can contain
# # as many variables as you wish. Lists can also be iterated over in a very simple manner.
# # Here is an example of how to build a list.
#
# alist=[1,2,5,75,98,"hello", "ab","",99]
#
# print(type(alist))
#
# print (alist[0])
# print((alist[6]))
# #slicing
# print(alist[2:5])
# print(alist[-4])
# print(alist[-2])
# print(alist[4:])
# print(alist[:4])
#
# # Lists also support operations like concatenation:
# blist=[59,"xx","world"]+alist
# print(blist)
#
# # Unlike strings, which are immutable, lists are a mutable type, i.e. it
# # is possible to change their content:
# blist[1]="yy"
# # print(blist)
# # print(len(blist))
# # blist[:5]=["tt",11]
# # print(blist)
#
# # List methods
#
# # You can also add new items at the end of the list, by using
# # the append() method
#
# blist.append("pp")
#
# print(blist)
#
# # list.remove(x)
# # Remove the first item from the list whose value is equal to x.
# # It raises a ValueError if there is no such item.
#
# blist.remove("pp")
# print(blist)
#
# del blist[0]
# print(blist)
#
# # list.insert(i, x)
# # Insert an item at a given position. The first argument is the index of the element
# # before which to insert, so a.insert(0, x) inserts at the front of the list,
# # and a.insert(len(a), x) is equivalent to a.append(x).
# blist.insert(7, 99)
# print(blist)
#
#
# # list.count(x)
# # Return the number of times x appears in the list.
#
# print(blist.count(99))
#
# # list.reverse()
# # Reverse the elements of the list in place.
#
# blist.reverse()
# print(blist)
#
# # list.pop([i])
# # Remove the item at the given position in the list, and return it. If no index is specified,
# # a.pop() removes and returns the last item in the list. (The square brackets around the i in
# # the method signature denote that the parameter is optional, not that you should type square
# # brackets at that position.)
# print(blist.pop(6))

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

result=0

for i in alist:
    result+=i
    #print (i, result)

result_list=[]
for i in alist:
    result_list.append(i+10)

#print(result_list)



blist=[i+10 for i in alist]
print(blist)


result_list2=[]
for i in alist:
    if i>=5:
        result_list2.append(i)
print(result_list2)

result_list2=[i for i in alist if i>=5]
print(result_list2)

result_list2=[i>=5 for i in alist]
print(result_list2)