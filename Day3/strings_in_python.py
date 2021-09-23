## PYTHON DATA TYPES: String###

"""Strings.
Besides numbers, Python can also manipulate strings, which can be
expressed in several ways. They can be enclosed in single quotes ('...')
or double quotes ("...") with the same result.
"""
# String with double quotes.
name_1="John"
name_2='John'

# \ can be used to escape quotes.
# use \' to escape the single quote or use double quotes instead.

a_string="doesnt"
print(a_string)

a_string='doesn\'t'
print(a_string)

# \n means newline.
b_string="Hello World.\n Today is beautiful"
print(b_string)

# Strings can be indexed, with the first character having index 0.
# There is no separate character type; a character is simply a string
# of size one. Note that since -0 is the same as 0, negative indices

word="Python"
print(word[0])
print(word[3])
print(word[4])
print(word[-4])

# In addition to indexing, slicing is also supported. While indexing is
# used to obtain individual characters, slicing allows you to obtain

print(word[1:4])

print(word[-3:-1])

# Note how the start is always included, and the end always excluded.
# This makes sure that s[:i] + s[i:] is always equal to s:

a_var="Hello"
b_var="World"
ab_var=a_var+" "+b_var
print(ab_var)

ab_var=a_var[1:3]+" "+b_var[-3:-1]
print(ab_var)

# Python strings cannot be changed — they are immutable. Therefore,
# assigning to an indexed position in the string
# results in an error:

a_var[3]="x"
print(a_string)

# The built-in function len() returns the length of a string:
characters = 'supercalifragilisticexpialidocious3456'
print(len(characters))

"""Basic operations

Strings can be concatenated (glued together) with the + operator,
and repeated with *: 3 times 'un', followed by 'ium'
"""

word="Python"
print(word*2)


 # String Methods
a_string=" Hello world.Today is Beautiful."
print(a_string)
# The strip() method removes any whitespace from the beginning or the end.
strip_=a_string.strip()
print(strip_)
# The lower() method returns the string in lower case.
lower_=a_string.lower()
print(lower_)

# The upper() method returns the string in upper case.
upper_=a_string[:13].upper().strip()
print(upper_)
# capitalize() Converts the first character to upper case
cap=a_string.capitalize()
print(cap)
# title () Converts the first character of each word to upper case
title_=a_string.title()
print(title_)
# The replace() method replaces a string with another string.
replace_=a_string.replace("Hello","Bye")
print(replace_)

# The split() method splits the string into substrings if it finds instances of the separator.
a_string="Hello world. Today is Beautiful."
split_=a_string.split()
print(split_)
print(type(split_))
# join() methods convert a list to string
join_=" ".join(split_)
print(join_)
print(type(join_))

# endswith()
endswith_=a_string.endswith("!")
print(endswith_)
# startswith()
startswith_=a_string.startswith("Hell")
print(startswith_)
#  count () returns the number of times a specified value occurs in a string.
count_=a_string.count("x")
print(count_)
# looping in string
for i in a_string.split():
    if i.count("o")>=1:
        print (i)
    else:
        print("False")

for i in a_string:
    if i =="o":
        print (i, "there is a o")
    else:
        print(i, "there is NO a o")

a_string="Hello world. Today is Beautiful."
alist=[i for i in a_string.split() if i.endswith(".")]
print(alist)
alist=" ".join([i for i in a_string.split() if i.endswith(".")])
print(alist)
# reverse a string

reverse=a_string[::-1]
print(reverse)

result=""
count=len(a_string)-1
print(count)
for i in a_string:
    result+=a_string[29]
    count-=1


print(result)

formatting in strings
a="New York"
b="Los Angales"
c="is beautiful than"

# manual
result=a+" "+c+" "+b
print(result)
# format()
result="{x} {y} {z}. I do not agree".format(z=b,y=c,x=a)
print(result)
# f string
result=f"{a} {c} {b}. I do not agree"
print(result)
# %
result="%s %s %s. I do not agree" % (a,c,b)
print(result)

name="Hasim"
lname="Engin"
age=35
result="Hi my name is {} {}.I am {} years old".format(name, lname, age)
result=f"Hi my name is {name} {lname}.I am {age} years old"
print(result)