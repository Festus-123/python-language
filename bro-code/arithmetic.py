# basic arithmetic operatons
# the increament operations #

friends = 1
friends += 1
print(friends)

friends-= 1
print(friends)
# we can perfothis operation with basic arithmetic operations * / +  % - ^^ and so on 
# and all could br augmnted or written plainly #

# round()
x = 3.12333
y = 58
z = 3

print(round(x))
# then there is the abs()
# value away from zero
# #
print(abs(-z)) # the output will stil be the same as the value of z weather having - or not
print(max(x, y, z))# prints out the max balue of the variables
print(min(x, y, z)) #prints out the min value of the three variables

# woring with tke math module we have to first import it as it is a builtin module for python
# this would enable us to use some methods and value like constants and perform mathemtical 
# actions like multiplication to the top an bttom, significant figures and so on#

import math

multiples_value = 13.5858038757983
print( math.floor(multiples_value) ) # this would round down this value down
print(math.ceil(multiples_value)) # this wil round this number down

print(math.pi )
print(math.e)
# print(math.remainder(multiples_value / 4))

# the math moduleproide a lot of math util for working with mathematical calculatons and
# othe math operations  #