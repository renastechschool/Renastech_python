
#DAY 1

### PYTHON SYNTAX  #####

# 1- Indentation
# Python reads code line by line. Therefore code block needs to be intended
# 2. For example code snap below is a code block, and second line needs to be intended
a=3
b=6
if a<b:
    print ("True")
# 2- Variables #
# 2.1. Creating a variable
x=2
y="hello world"
print(x)
# 2.2. Getting type of a variable
  # type() function gives type of a variable
print(type(y))
# 2.3. Single quotes versus double quotes
 # a string variable can be declire "" or ''
aVar="hello"
bVar='World'
print( aVar, bVar)
# 2.4. Variables are case sensitive
 # these are two different variables
A="b"
a="c"
# 2.5. Rule of creating a variable
  # a variable can not start with a number
  # a variable should not have a space
#2var=4
## 2.6. Many to one assignment ()
z=y=x="Hello"
print (x)
print(y)
print(z)

# 2.7. Many to many assignment (unpacking)
x, y, z="World", "Hello","Today"

print (x)
print(y)
print(z)
# 2.8. Reserve words for variable names
  # Reserve works should not be used as variable such as int, str, and, or ...
int=5
str="hi"

# 3. Comments
# 3.1 Single line comments
# this is a comment
#### this is a second comment
# 3.1 Multiple comments
"""This is a 
multiline 
comment
"""


