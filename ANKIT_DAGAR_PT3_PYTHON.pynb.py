#Name:- Ankit Dagar
#Class -CSE 4 A
#Roll Number :- 2K18CSUN01053
#PYHTON :- PT3

#----------------------------------------------#
#Theoretical Questions:-
#Q1.) What is the syntax to call a constructor of a base class from child class.
#A1.) To call a constructor of a base class from child class,:-
#   we call using super()Command.

#Q2.) How is a class made as inherited class (syntax of child class).
#A2.) class Parent:
#   pass
#       class Child(Parent):
#           pass
#Child class inherit the Parent class.

#Q3.) Print an element of a nested dictionary.
#A2.) Student = {1: {'Name': 'Ankit-Dagar', 'Age':'19','Class': 'CSE-4A', 'sex': 'Male', 'Year':'Second'},
#    2: {'Name': 'Anish- Stud ', 'Age':'20','Class': 'CSE-2A', 'sex': 'Male', 'Year':'First'}}

#print(Student)

#----------------------------------------------#

#SET-C

#Q1. :- Write a program that calculates and prints the value according to the formula given below.
#Take three values from user. Q= square root (( 2*value1*value2)/value3)

#ANS 1 :-
import math
def sqrroot (value1,value2,value3):
    Q=math.sqrt(( 2*value1*value2)/(value3))
    return Q

value1 =int(input("Enter value1 :- "))
value2 =int(input("Enter value2 :- "))
value3 =int(input("Enter value3 :- "))

sqrroot = sqrroot (value1,value2,value3)

print ("Q = ", sqrroot)

#------------------------------------------------------------#

#Q2. Please write a program which accepts a string from console and print the characters that have even indexes.
#ANS 2 :-
print("Please enter text to print::")
inputchars = input()

if inputchars:
    string = ""
    for i in inputchars:
        if inputchars.index(i) % 2 == 0:
            string += str(i)

print('-------------------ANKIT--DAGAR-----')
print("You Entered:", inputchars)
print("Result:")
print(string)

#-------------------ANKIT--DAGAR----------------------#


