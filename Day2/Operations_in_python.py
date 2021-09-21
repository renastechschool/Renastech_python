
## PYTHON OPERATORS ###
"""Arithmetic operators
Arithmetic operators are used with numeric values to perform common mathematical operations
"""
x= 43
y=9

# Addition.
print(x+y)

# Subtraction.
print(x-y)

# Division.
# Result of division is float number.
print(x/y)

# Floor division.
print(x//y)

# Modulus.
print(x%y)

# Exponentiation.
print(x**y)

"""Assignment operators

Assignment operators are used to assign values to variables
"""
# Assignment: =
number=5
print(number)

# Multiple assignment.
# The variables first_variable and second_variable simultaneously get the new values 0 and 1.
first_variable, second_variable=1,2
print(second_variable)

# You may even switch variable values using multiple assignment.
second_variable,first_variable=1,2
print(second_variable)

# Assignment: +=
number=5
number +=3
number =number+3
print(number)

# Assignment: -=
number -=2
print(number)

# Assignment: *=
number *=5
print(number)

#Assignment: %=
number %=7
print(number)

# Assignment: //=
number *=40
number //=6
print(number)

"""Comparison operators
Comparison operators are used to compare two values.
"""
number_1=5
number_2=8

# Equal.
print(number_1==number_2)

# Not equal.
print(number_1 !=number_2)

# Greater than.
print(number_1 > number_2)

# Less than.
print(number_1 < number_2)

# Greater than or equal to
print (number_1 >= number_2)

# Less than or equal to
print (number_1 <= number_2)


"""Identity operators
Identity operators are used to compare the objects, not if they are equal, but if they are actually
the same object, with the same memory location.
"""

first_fruit="banana"
second_fruit="banana"
third_fruit==first_fruit

# is
# Returns true if both variables are the same object.
# first_fruits_list and third_fruits_list are the same objects.
print(first_fruit is second_fruit)
print(first_fruit is third_fruit)

# is not
# Returns true if both variables are not the same object.
# Example:
# first_fruits_list and second_fruits_list are not the same objects, even if they have
# the same content
print(first_fruit is not third_fruit)

"""Logical operators
Logical operators are used to combine conditional statements.
"""

first_variable=7
second_variable=10

# and
# Returns True if both statements are true.
print (first_variable > 0 and second_variable <11)

# or
# Returns True if one of the statements is true
print (first_variable > 0 or second_variable <9)

# not
# Reverse the result, returns False if the result is true.
print( not first_variable == second_variable)

"""Membership operators
Membership operators are used to test if a sequence is presented in an object.
"""
a_fruit="banana"

# in
# Returns True if a sequence with the specified value is present in the object.

# Returns True because a sequence with the value "banana" is in the list
print ("a" in a_fruit)

# not in
# Returns True if a sequence with the specified value is not present in the object

# Returns True because a sequence with the value "pineapple" is not in the list.

print ("x" not in  a_fruit)

