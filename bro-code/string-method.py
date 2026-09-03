# String methods in python.. #
# len()  this is a method to determine the lenght of a string 

name  = "festus phillip aebola" # this counts the spaces as well 
phone_no = "080-408-095-27"
print (len(name))

# preceeding a varible with a dot provides us with vaious properties and methods to pick from
# name.find() this find the givees the first occurence of a given instance 
#working with indexes starts count with zero

print(name.find(" "))

# to find the last occurence we use rfind
print(name.rfind(" ")) # r meaning reverse 

# if python couldn't locate a given value it returns a -1

# another method is capitalise() ---this returns a capital value of string(s)


print(name.capitalize()) # inthis case only the first letter is capitalised sine it is one case 

# uding the upper method will take all character in a string and make it al uperCase

print(name.upper()) # also we have lower- to make it lower case 

# we also have the isdigit() method this returns a boolean 
# if te string is all digit it returns true else it return fals 
print(name.isdigit())

# isalpha() method 
# this return a boolean true or false if a string contains only alphabetical-character
# note whiespace is not an alphabetical character so if any it would return false 

print(name.isalpha())

# we also have the count method 
# we can use this to count the number of a character in a string weather spces of symbols or even a 
# letter or a number 
#  #

print(phone_no.count("0"))

# we also have the replace method 
# we can replace an occurence of one charater with another 

print(name.replace(" ", "-"))


# to get a comprehensive list of all of the string method available to python? 
# use the help () method and print the result 
# note to put in what you getting help for 
# in this case we use help(str)

# print(help(str)) 

# simple excersise validating user input


# indexing
credicCard_number = "1234-5678-1313-7373737"
# if i meed the first character in this string it coud be accessed through indexing



# String methods in python.. #

# string indexing
# alloes aessing element of a sequence using [] 
# indexing operator
# [start, end, step] 
# [] called an indexing operator # 

print(credicCard_number[0])
# this would return the first number in the string cause in the case of index it starts 
# counting from zero

# now based on the method stated above about regarding start end andstep
# in this case if you have just one position filled in the index it only rerfers to the 
# starts like  the example stated above
# 
# if we want the first numbered digit of our string maybe 5 #

print(credicCard_number[0:4]) # output will be 1234 the dash wouldn't be placed there since it
# is the fourt index so we exclude it 
# the strting index is inclusive but the ending index isexclusive
# in a case where we want to write it and reduce context and still achieve result we short it  #

print(credicCard_number[:4]) # in reverse if we require everything from a start point up to
# the end we write 
print(credicCard_number[5:]) # this il output from the 5th index to the end of the string

# to get the last digit or character of the string we use negative 1
#  #
print(credicCard_number[-1]) # this will return the value of the last output 
# incrementing the value of the ngative number will keep indexing just this time it would 
# be from behing e.g print(cread..[-4]) will give a value from 4 backward's count

# using steps we access the character of a string along A map like count 
# probabky increaments of 2 or 3 or more accross the string characters  #

print(credicCard_number[::2]) # if we aren't filling in the start or end and want to use steps
# we use double colons to spicify that starts and end are it default but we 
# print every 2nd character in our string increamentally

# to reverse a string we set the step insde to be -1