
"""Sets.

A set is a collection which is unordered and unindexed.
In Python sets are written with curly brackets.

Set objects also support mathematical operations like union, intersection, difference, and
symmetric difference.
"""

"""Sets"""

# set example
aset={"a", "b", "c", "d"}
print(type(aset))
# It is also possible to use the set() constructor to make a set.
# Note the double round-brackets
aset=set(("a", "b", "c", "d"))
print(type(aset))
bset={"a", "b", 'c', "d", "a"}
print(bset)
#print(bset[0]) # error

# You may check if the item is in set by using "in" statement
print("a" in aset)
print("f" not in aset)

# ==set methods==#

# Use the len() method to return the number of items.
print(len(bset))
# You can use the add() object method to add an item.
bset.add("f")
print(bset)
# you can join two set by using update () method
aset.update({"x","y"})
print(aset)
# Use remove() method to remove an item.
aset={"a", "b", "c", "d"}
aset.remove("b")
print(aset)
# Use pop() remove  a random item from a set
aset.pop()
print(aset)

# set operations
# Demonstrate set operations on unique letters from two word:
python="python is very easy"
java="java is very fast"
python_set=set((python))
java_set=set((java))
print(python_set, java_set)
# Letters in first word but not in second with difference () method

python_java=python_set.difference(java_set)
python_java2=python_set-java_set
print(python_java)
# Letters in first word or second word or both with union() method
python_java_union=python_set.union(java_set)
python_java_union=python_set | java_set
print(python_java_union)

# Common letters in both words with intersection() method
python_java_int=python_set.intersection(java_set)
python_java_int=python_set & java_set
print(python_java_int)


# lopping in sets

for i in python_set:
    print(i)