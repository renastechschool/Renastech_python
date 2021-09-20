# ## PYTHON OPERATORS ###
# """Arithmetic operators
# Arithmetic operators are used with numeric values to perform common mathematical operations
# """
# x=89
# y=9
#
# # Addition.
# z=x+y
# print(z)
#
# # Subtraction.
# k=x-y
# print(k)
#
# # Division.
# # Result of division is float number.
# result=x/y
# print(result)
#
# # Floor division.
# result=x//y
# print(result)
#
# # Modulus.
# result=x%y
# print(result)
#
# # Exponentiation.
# result=x**y
# print (result)
#
#
# #math opreration
# result=((x+y)//6)%3
# print(result)
#
# # get adress location of a abject
# print (id(result))
# """Assignment operators
# Assignment operators are used to assign values to variables"""
#
# # Assignment: =
#
# avar="Hello"
#
# # Multiple assignment.
# # The variables first_variable and second_variable simultaneously get the new values 0 and 1.
# first_variable, second_variable = 1,0
# print(first_variable)
#
# # You may even switch variable values using multiple assignment.
# second_variable ,first_variable= 1,0
#
# # Assignment: +=
# a=9
# a+=10
# a=a+10
# print(a)
#
# # Assignment: -=
#
# a-=10
# print(a)
# # Assignment: *=
#
# a*=10
# print(a)
#
#
# #Assignment: %=
#
# a%=11
# print(a)
#
# # Assignment: //=
#
# a//=4
# print(a)

#
sentence="Hello World"

#
c=0
b=0
for i in sentence:
    if i in ("a","e","o","u","i"):
        print(i)
        c+=1
    else:
        print(i)
        b+=1


print(c)
print(b)

"""Comparison operators
Comparison operators are used to compare two values."""

num1=5
num2=8

print(num1==num2)
print(num1!=num2)

print(num1>num2)

"""Identity operators
Identity operators are used to compare the objects, not if they are equal, but if they are actually
the same object, with the same memory location.
"""

