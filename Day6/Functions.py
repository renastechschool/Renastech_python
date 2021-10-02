
"""Function Definition

The keyword def introduces a function definition. It must be followed by the function name and the
parenthesized list of formal parameters. The statements that form the body of the function start at
the next line, and must be indented.
"""
#Syntax of creating a function

# def function_name(parameter1, parameter2):
#        # function body
#        # write some action
#     return value

def greet():
    print("Welcome")

greet()

def greet2(name):
    print("Welcome "+name)

greet2("John")

# Usually a function created one or more parameters

def message(first_name, last_name):
    full_name=first_name +" "+last_name
    print(full_name)

message("John","Smith")


# default argumnets in a function
def who_are_you(first_name, last_name, country="USA"):
    full_name = first_name + " " + last_name
    country_=country
    print(full_name, country_)


who_are_you("Ahmet","Demir")

who_are_you("Ahmet","Demir", "Turkey")

#Calling a function
#Once we defined a function or finalized structure, we can call that function by using its name.
#We can also call that function from another function or program by importing it.
#To call a function, use the name of the function with the parenthesis,
#and if the function accepts parameters, then pass those parameters in the parenthesis

def even_odd(n):
    """" This gives you if a number even or odd
    n should be an interger value"""
    if n % 2==0:
        print( "{} is a even number".format(n))
    else:
        print(f"{n} is odd number")

even_odd(111)
even_odd(110)

#Calling a function of a module
#You can take advantage of the built-in module and use the functions defined in it.
#For example, Python has a random module that is used for generating random numbers and data.
#It has various functions to create different types of random data.

#Letâ€™s see how to use functions defined in any module.
#First, we need to use the import statement to import a specific function from a module.
#Next, we can call that function by its name.

def get_sqrt(n, k):
    return n**k
sq=get_sqrt(6, 3)

print(sq)

import math
print(math.pow(6,3))

from  math import pow
print(pow(6,3))

print(pow(8,3))



##========================================================================##
#Docstrings
#In Python, the documentation string is also called a docstring.
#It is being declared using triple single quotes (''' ''') or triple-double quote(""" """).

#We can access docstring using doc attribute (__doc__) for any object like list, tuple, dict, and user-defined function, etc.

def factorial(x):
    """This function returns the factorial of a given number.
    x should be an integer """
    return x

# access doc string
print(factorial.__doc__)

#When you use the help function to get the information of any function, it returns the docstring.
# pass function name to help() function
print(help(pow))
print(help(even_odd))
print(even_odd.__doc__)

#Scope
#When we define a function with variables, then those variablesâ€™ scope is limited to that function.
#In Python, the scope of a variable is an area where a variable is declared. It is called the variableâ€™s local scope.
#We cannot access the local variables from outside of the function.
#Because the scope is local, those variables are not visible from the outside of the function.global_lang = 'DataScience'

global_var="java"

def has_local_var():
    local_var="python"
    return local_var

print(global_var)
print(local_var)

has_local_var()

#Function Arguments

#The argument is a value, a variable, or an object that we pass to a function or method call.

#Positional Arguments:
#Positional arguments are arguments that are pass to function in proper positional order.
#That is, the 1st positional argument needs to be 1st when the function is called.
#The 2nd positional argument needs to be 2nd when the function is called

def add(a,b):
    return a/b

x=add(90,6)

y=add(6, 90)

z=x+8
print(z)


#Keyword Arguments:
#A keyword argument is an argument value,
#passed to function preceded by the variable name and an equals sign
#In keyword arguments order of argument is not matter, but the number of arguments must match

def get_age(dob, year):
    age=year-dob
    return age

cal_age=get_age(1980, 2021)
print(cal_age)

cal_age2=get_age(year=2021, dob=1980)
print(cal_age2)

#Default Arguments:

#Default arguments are arguments that take the default value during the function call.
# If we do not pass any argument to the function, then the default argument will take place.
#We can assign default values using the = assignment operator
# function with default argument
def message(name="Hasan"):
    print("Hello", name)
message()
message("John")


#Variable-length Arguments:
#In Python, sometimes, there is a situation where we need to pass multiple numbers of arguments to the function.
#Such types of arguments are called variable-length arguments.
#We can declare a variable-length argument with the * (asterisk) symbol

def sum_square(*numbers):
    sum=0
    for i in numbers:
        x=i**2
        sum+=x
    return sum
get_sq=sum_square(1,2,3,4,5,6)
print (get_sq)

get_sq=sum_square(1,2,3,4,5,6, 80, 9)
print (get_sq)

def join_words(*words):
    sentece=""
    for i in words:
        sentece+=i
        sentece+=" "
    return sentece

get_sentence=join_words("I", "am", "a", "student", ".")
print(get_sentence)


#Python Anonymous/Lambda Function:

#Sometimes we need to declare a function without any name.
#The nameless property function is called an anonymous function or lambda function
#Syntax of lambda function:

# lambda: argument_list:expression

x = lambda a : a + 10
print(x(5))

x = lambda a, b : a * b
print(x(5, 6))

#filter() function in Python
#In Python, the filter() function is used to return the filtered value.
#We use this function to filter values based on some conditions
#Syntax of filter() function:

# filter(function, sequence)

def more_than_zero(n):
    if n>0:
        return n
y=more_than_zero(6)
print(y)

y=more_than_zero(-6)
print(y)

alist=[1,4,6,-7,-3,5,-9,0]

get_numbers=list(filter(more_than_zero, alist))

print(get_numbers)

get_numbers2=list(filter(lambda x:x>0, alist))
print(get_numbers2)

a_string="Hello world"
get_subset=list(filter(lambda x: x not in ("a", "e","i", "o", "u"), a_string))
print(get_subset)


##========================================================================##
#map() function in Python
#In Python, the map() function is used to apply some functionality for every element present
#in the given sequence and generate a new series with a required modification
#Syntax of map() function:

#map(function,sequence)

a_list=[2,56,8,9,35,89,12]
square=list(map(lambda x:x**2, a_list))
print(square)


def make_square(*nums):
    result=[]
    for i in nums:
        result.append(i**2)
    return result


sum_numbers=lambda x,y:x+y

print(sum_numbers(2,5))


