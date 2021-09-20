# User Input

#Exercise 1: Categorize a person for covit-19 risk based on his/her age:
high_risk=65
mid_risk=50
low_risk=30
very_low_risk=20

age=input("What is your age?")

name=input ("What is your name?")
age=int(age)
print (type(age))
print (type (high_risk))

if age >=high_risk:
    print ("Hi "+ name +".You are in high risk becasue your age is " +str(age))
if age <high_risk and age >=mid_risk:
    print ( "Hi" + name +".You are in mid risk becasue your age is " +str(age))

if age <mid_risk and age >=low_risk:
    print ( "Hi "+ name +".You are in low risk becasue your age is " +str(age))
if age <=very_low_risk:
    print ( "Hi "+ name +".You are in very low risk becasue your age is " +str(age))

