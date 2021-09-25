
"""Dictionaries.

A dictionary is a collection which is ordered, changeable and indexed. In Python dictionaries are
written with curly brackets, and they have keys and values.

Dictionaries are sometimes found in other languages as “associative memories” or “associative
arrays”. Unlike sequences, which are indexed by a range of numbers, dictionaries are indexed by
keys, which can be any immutable type; strings and numbers can always be keys. Tuples can be used
as keys if they contain only strings, numbers, or tuples; if a tuple contains any mutable object
either directly or indirectly, it cannot be used as a key. You can’t use lists as keys, since
lists can be modified in place using index assignments, slice assignments, or methods like append()
and extend().

It is best to think of a dictionary as a set of key: value pairs, with the requirement that the
keys are unique (within one dictionary). A pair of braces creates an empty dictionary: {}.
Placing a comma-separated list of key:value pairs within the braces adds initial key:value pairs
to the dictionary; this is also the way dictionaries are written on output.
"""
# # Create a dictionary
# # create a dictionary using {}
# adict={"name":"Mark","last_name":"white","age":45,"city":"New York"}
# print(adict)
# print(type(adict))
# # create a dictionary using dict()
# adict=dict({"name":"Mark","last_name":"white","age":45,"city":"New York"})
# print(adict)
# print(type(adict))
# # create a dictionary from sequence having each item as a pair
# bdict=dict([("name", "hasim"),("last_name","engin"), ("age", 35)])
# print(bdict)
#
# # ==accessing elements in a dictionary== #
# # You may access set elements by k
# print(adict["name"])
# # You may access set elements by keys with get() method.
#
# print(adict.get("name"))
#
# # ==check membership == #
# # To check whether a single key is in the dictionary, use the in keyword.
# print("name" in adict)
# print("name" in adict.values())
# print(45 in adict.keys())
# print("Aydin" in adict.values())
# # ==updating a dictinoary==#
# # update a value by using a key
# adict["name2"]="Aydin"
# print(adict)
#
# adict["name"]="Aydin"
# print(adict)
#
# adict["names"]=["Aydin", "hasim", "hasan"]
#
# # Add new key/value pair to the dictionary
# # Add new key/value pair to the dictionary with update()
#
# adict.update({"cities":["florida", "boston"]})
# print(adict)
#
# # ==dictionary methods== #
# # Get keys from a dictionary with keys() method
# adict_keys=adict.keys()
# adict_keys=list(adict.keys())
# print(adict_keys)
# print(type(adict_keys))
# # # Get values from a dictionary with values() method
# adict_values=adict.values()
# adict_values=list(adict.values())
# print(adict_values)
# # Get all key-value pair with items() method
# adict_items=adict.items()
# adict_items=list(adict.items())
# print(adict_items)
# # you can get lenght of a dict with len() function
# print(len(adict))
# # It is also possible to delete a key:value pair with del .
# del adict["city"]
# print(adict)
# # It is also possible to delete a key:value pair with pop () method .
# print(adict.pop("name"))
# print(adict)
# # You can remove all items in a dict with clear() method
# #adict.clear()
# print(adict)

#We can iterate through a dictionary using a for-loop and
# access the individual keys and their corresponding values.

adict={"name":"Mark","last_name":"white","age":45,"city":"New York"}
for i in adict.values():
    print(i)

for i in adict.keys():
    print(i)

result={}
for x, y in adict.items():
    result[y]=x
print(adict)
#print(result)

for x in adict.keys():
    if adict[x]==45:
        adict[x]="Aydin"

key_list=[]
value_list=[]
for x, y in adict.items():
    key_list.append(x)
    value_list.append(y)

print(key_list, value_list)

result2={}

for x, y in zip(key_list, value_list):
    result2[x]=y

print(result2)
#print(adict)