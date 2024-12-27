from functools import total_ordering


print("i","love","python")#interesting way to use a print function with comma as a separator
print("i" "love" "python")#space as a seperator
print("jai shree ram"*7)#with repeat character
print("where","there","is","a","will","there","is","a","way")#comments
#multiline comments are same as single line comments.
#docstring comment
"""this is single line docstring comment"""
"""this is
the comment written
in more than one line
"""
#identifier
#variable only contain alpha-numeric and underscorecharacter.it should not start with number
#var 1 is not a valid variable
s="arti"
print(s)
#python keyword there are 33 keyword in python 3.5 and 35 keywords in python 3.7and3.11
import keyword
print(keyword.kwlist)
print(keyword.iskeyword("and"))
print(keyword.iskeyword('supriya'))
#in python we can change type of the variable after it has been set once (or initialised with some other type
# the most commonly used data types in python are:Numbers,List,Tuple,strings,dictionary
# associating a value with a variable using the assignment operator (=)is called as binding)
s=t=f=p=23 #this is called chained assigment.
#multiple assigment
ram,shayam,rita,sita=20,19,21,23
#variable-container to store a value
#keyword-reserved words in python
#identifiers-class/function/variable name
#input()function
a=input("a: ")
#expression:an expression is the combination of values(constant),variables,and operators
#1.constant expression 2. arithmetic expression
x=97
y=99
add=x+y
sub=x-y
multiply=x*y
divide=x/y
remainder=x%y
quotient=x//y
print(sub,add,multiply,quotient,remainder,divide)
