a = "1"
b = "2"
print(int(a)+int(b))
# converted string values of a and b to int,
# it is implicit conversion - by the language
# explicit conversion is done - by the programmer

#  implicit type Casting 
 
# Python automatically converts 
# a to int 
a = 7
print(type(a)) 
 
# Python automatically converts 
# b to float 
b = 3.0
print(type(b)) 
 
# Python automatically converts 
# c to float as it is a float addition 
c = a + b 
print(c) 
print(type(c))
 
# Python automatically converts 
# d to float as it is a float multiplication
d = a * b
print(d)
print(type(d))

#explicit type Casting 
 
# int variable
a = 5
 
# typecast to float
n = float(a)
 
print(n)
print(type(n))