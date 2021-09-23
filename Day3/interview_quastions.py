##What is PYTHONPATH?

##Ans: It is an environment variable which is used when a module is imported. Whenever a module is imported,
##PYTHONPATH is also looked up to check for the presence of the imported modules in various directories.
# The interpreter uses it to determine which module to load.

import os
import numpy
os.getcwd()
import sys
sys.path.append(r'C:\Users\hengin\Documents\xxx')
for i in sys.path:
    print (sys.path)


x='I don\'t like it'
##Is indentation required in python?
##Ans: Indentation is necessary for Python. It specifies a block of code. All code within loops, classes, functions, etc is specified within an indented block.
##It is usually done using four space characters. If your code is not indented necessarily, it will not execute accurately and will throw errors as well.



### Explain In built Data Structures of python?
# Ans: There are mainly four types of data structures in python.
# 1. Lists: List is a collection of heterogeneous data items from integers to strings even another list.
# Lists are mutable. lists do the work of most of the collection data structures found in other languages.
# A list is defined in [ ] brackets. Ex: a = [1,2,3,4]
# 2. Sets: A set is an unordered collection of unique elements. set operations like union | ,
# intersection &and difference — can be applied to a set. sets are immutable. () are used to represent a set.
# Ex: a={1,2,3,4,}
# 3. Tuple: Python tuples work exactly like Python lists except they are immutable. () use to define a tuple.
# Ex: a = (1,2,3,4)
# 4. Dictionary: Dictionary is a collection of key-value pairs. it is similar to the hash map in other languages.
# In Dictionary Keys are Unique and immutable objects.
# Ex: a = {‘numbers’:[1,2,3,4]}

### Explain //,% and * *operators in python?
# Ans:
# // (Floor Division)- It is a division operator that returns the integer part of the division.\
#     Ex: 5//2=2
# % ( Modulus)- It returns the remainder of the division.
# Ex: 5%2=1
# ** (Power)- It performs an exponential calculation on the operator. a**b means a raised to the power of b.
# Ex: 5**2=25, 5**3 = 125
### Difference Between append (), extend (), and insert() in python. Explain with an example?

# Ans: append: It is used to add new elements at the end of the list.
# insert: It is used to add an element at a particular position in the list.
# extend: It is used to extend the list by adding a new list.
numbers = [1,2,3,4,5]
numbers.append(6)
print(numbers)

numbers.insert(2,7)  ## insert(position,value)
print(numbers)
#[1,2,7,4,5,6]
numbers.extend([7,8,9])
print(numbers)
#[1,2,7,4,5,6,7,8,9]
numbers.append([4,5])
#[1,2,7,4,5,6,7,8,9,[4,5]]

## what is slicing?

### Differentiate remove, del, and pop in python?
numbers = [1,2,3,4,5]
numbers.remove(1)
del numbers[0]
numbers.pop()
print(numbers)