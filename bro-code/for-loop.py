
# for loops in python
# execute a block of code a fixed number of times 
# you can iterate over a range, string, sequence etc 
# 
# basic syntax of for loops #

for x in range(1, 11):
    print(x)

# x is not a compulsary part of the syntax 
# to alt this syntax to count reversely we use the reverse method 

for x in reversed(range(1, 11)): # this print the value of x in reversal
    print(x)

#just like indexing we have the start the end nd the step by adding another figure like 
# range(1, 10, 3) the last figure indicates the step i.e the distance or gap in which it itertes 

for x in range(1, 11, 3):
    print(x)

# apart from the range function we cam iterate over something elselike a string or so #

credit_Card = "1234-5678-9012-3456"

for x in credit_Card:
    print(x) # we  could also iterate in astring using the method

# we could also use continue and break in a for loop ass well #

for i in range(1, 22):
    if i == 13:
        continue # this would skip over a particular iteration 
        # break this would instead break the loop once this condition is true 
    else:
        print(i)