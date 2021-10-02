"""IF statement
"""
# if statement
number=6
if number >4:
    print("{} is greater than 4". format(number))
    print(f"{number} is greater than 4")
    print(str(number)+" is greater than 4")

# if else statement
password=124
if password==123:
    print( "Password is correct")
else:
    print("Password is incorrect")

## if elif and else statement

num=3
if num==1:
    print("Number is "+str(num))
elif num>1:
    print("Number is greater "+str(num))
elif num<1:
    print("Number is smaller "+str(num))
else:
    print("I do not know")

# nested if else statement

num1=3
num2=6
if num1 < num2:
    if num1> 0:
        if num1<4:
            print(num1)
else:
    print(num1)
