import time

# the sleep function of the time module allows out program to sleep for a 
# given time before execution

my_time = int(input("enter time in seconds "))

# 9
# another way toreverse is using negative steps 

for i in range(my_time, 0, -1):
    seconds = i % 60
    minutes = int((i / 60)) % 60
    hours = int(i / 3600)
    print(f"{hours:02} {minutes:02} {seconds:02}")
    time.sleep(1)

print("TIMES's UP!")