#While loop in python 
#  A while loop will execurte some code while some conditionns are true 
#  #
# exmaple 
name = input("enetr your name")

if name == "":
    print("you did not enter a name ")
else:
    print(f"hello{name}")

# what this doesisthat it check the condition once and when it remains true it execute the code once 
# and move on to the next instance 
# 
# the usefulness of while loop is that is we want the user to compularily enter their name we could 
# keep prompting the user for their name 
#  #
     # as long as this remains true we keep prompting the user for name until its false

while name == "":
    print("you didn't enetr a name ")
    name = input("enter your name")
print(f"hello{name}")

# we would need a way to break out of loop to avoid infinite loop
# while looop with logical operators

food = input("enter a foodyou like (enter q to quit)")

while not food == "q":
    print(f"you like {food}")
    food = input("enter a foodyou like (enter q to quit)")

print("bye bye ")


num = int(input("enter a number between 1- 10"))

while num < 1 or num > 10:
    print(f"{num} is not valid")
    num = int(input("enter a number between 1- 10"))
print(f"your number is {num}")

