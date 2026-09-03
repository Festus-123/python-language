# logical operators in python
# this alows evaluation of multiple condition {or, and, not}
# or--- at lest one condition must be true
# and--- both conditions must be true 
# not--- invrts the condition {not fase, not true

# the syntax for or--- is (or)
# the syntax of and is (and)
# the syntax of not is (not)

# example #


# OR #
temp  = 36
is_raining = True

if temp > 35 or temp < 0 or is_raining: # as long as one of this is true we do this code
    print("the outdoor event is clsed")
else:
    print("the outdoor event is still on")

#AND
temp = 30
is_sunny = True

if temp >= 30 and is_sunny: # this will only execute as longas both conditions are true 
    print("it is hot outside 🥵 and it is sunny as fucccckkk ☀️")
else :
    print("what the fuck is my business")

#NOT 

temp = 10
is_cloudy = False

if temp <= 20 and not is_cloudy: # this code will execute as long as the condition is not true 
    print("this is so fucking cruel why is the weather so cold ")
else:
    print("dammmmmmmmmmmmmmnn")

