"""Tuples.
A tuple is a collection which is ordered and unchangeable. In Python tuples are written with
round brackets.

The Tuples have following properties:
- You cannot change values in a tuple.
- You cannot remove items in a tuple.
"""


"""Tuples"""

fruits_nums=("apple", "banana",3,7)
print(type(fruits_nums))
print(fruits_nums[0])
print(fruits_nums[-1])
print(fruits_nums[0:3])

# You cannot change values in a tuple.
a_list=list(fruits_nums)
a_list[3]="cherry"
fruits_nums2=tuple(a_list)
print(fruits_nums2)
print(type(fruits_nums2))

# use len() coun item from a tuple
print(len(fruits_nums2))

a_tuple=1,3,5, "hello"
print(a_tuple)
print(type(a_tuple))

# Tuples may be nested:
b_tuple=5,9,"world"
ab_tuple=a_tuple+b_tuple
print(ab_tuple)

# The following example is called tuple packing:
x, y=4,6
print(x)

x, *y=4,6, 7
print(y)

x, y=4,6
print(x)
x,y=y,x
print(x)


## tuple methods
# you can get count of items with count()
b_tuple=(1,2,3,4,5,"hello",6,7,3,5,5)
print(b_tuple.count(5))

print(b_tuple.index("hello"))

for i in b_tuple:
    print(i)



