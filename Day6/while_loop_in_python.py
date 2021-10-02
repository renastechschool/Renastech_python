"""WHILE statement


The while loop executes as long as the condition remains true. In Python, like in C, any
non-zero integer value is true; zero is false. The condition may also be a string or list
value, in fact any sequence; anything with a non-zero length is true, empty sequences are
false.

The test used in the example is a simple comparison. The standard comparison operators are
written the same as in C: < (less than), > (greater than), == (equal to), <= (less than or
equal to), >= (greater than or equal to) and != (not equal to).
"""

"""WHILE statement"""

number=2
power=5
result=1

while power >0:
    result*=number
    print(power,result)
    power-=1
print (result)

count=3
while count <=25:
    print (count)
    count+=5

age=int(input("what is your age"))
while age >25:
    if age % 2== 0:
        print( "Your age is even number")
    else:
        print("Your age is odd number")
    age-=2
