# ### PYTHON DATA TYPES: String###
#
# """Strings.
# Besides numbers, Python can also manipulate strings, which can be
# expressed in several ways. They can be enclosed in single quotes ('...')
# or double quotes ("...") with the same result.
# """
#
# name_1="John"
# name_2='John'
# print(name_1==name_2)
#
# # \ can be used to escape quotes.
# # use \' to escape the single quote or use double quotes instead.
#
# a_string='I don\'t like apple'
#
# print(a_string)
#
# b_string="Bye world. \nToday is beautiful"
# print(b_string)
#
# # Strings can be indexed, with the first character having index 0.
# # There is no separate character type; a character is simply a string
# # of size one. Note that since -0 is the same as 0, negative indices
#
# b_string="Bye world.Today is beautiful"
# print(b_string[0])
# print(b_string[7])
# print(b_string[-7])
# print(b_string[7:])
# print(b_string[:7])
# print(b_string[7:11])
#
# # Python strings cannot be changed — they are immutable. Therefore,
# # assigning to an indexed position in the string
# # results in an error:
#
# alist=[1,2,3]
# alist[1]=5
# print(alist)
#
# b_string="Bye world.Today is beautiful"
#
# #b_string[6]="Z" # error
#
# b_string1=b_string[:10]
# b_string2=b_string[11:]
# b_string_result=b_string1+"Z"+b_string2
# print(b_string_result)
#
# # The built-in function len() returns the length of a string:
# characters = 'supercalifragilisticexpialidocious3456'
# print(len(characters ))
#
#
# """Basic operations
# Strings can be concatenated (glued together) with the + operator,
# and repeated with *: 3 times 'un', followed by 'ium'
# """
# #b_string_result=b_string_result*3
# print(b_string_result)
#
# print( " " in b_string_result)

my_name="Hasim"
my_age=35

name_age=my_name+" "+str(my_age)
print(name_age)



alist=[1,2,3,4,5,6,7,8]
alist=[str(i) for i in alist]
print (alist)

result="".join(alist)
print(result)