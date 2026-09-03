# type casting in python
# this is the process of converting a variable from one dta type to another 
# str() int() float() bool()  this are metods #
name = ""
age = 0
gpa = 4.8
is_student = True

# we can get the data type of a variable or a value with the type-method
print(type(name)) # this will be applicable to all data 

# using the specified methods above we can convert from one data type to another

gpa = int(gpa)
print(gpa) # this remove the decimal portion

age = float(age)
print(age)

age = str(age)
print(age) # this will appear the same but it s a string i.e it ca't be used in math calc
# but to determine weather it changes we use the typecast method we ttaked bout erlier  #
# print(type(age))

# typecasting to bool is kind of different 
# when converting a string to bool it would always becometrue except the string is empty
# but in an integer case #

name = bool(name)
print(name)

age = bool(age)
print(age)

# this is especially useful in handling user input
# in the case of converting their input to integer or checking ifit's empty or not 
# user'simput is always in string