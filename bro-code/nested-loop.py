# nested loop in py 
# a loop within another loop
# outer and inner 
# syntax of how nested loop looks like 
# outer loop:
#   inner loop:
#       and the rest of the code till we exit both loop by ending the indentation
# it could literarily be any loop inside any loop

# nested loop are a bitch
# 

# for i in range(5): # this will repeat the code three times except that it would be on a line 

#     for x in range(1, 10):
#         print(x, end=" ")   
#     print() # this avoids us repeating the exeuted code on a single line


     # this will return a vlue that is on seperate line becasue the defaultof it ends 
    # attribute is end="/n" to chnage this we change the default 
    #  now to creta e a nested loop we wrap the above loop inside an outer loop

rows = int(input("enter no of rows: "))
colums = int(input("enter a number of collums: "))
symbol = input("enter a symbol")


for i in range(rows):
    for x in range(colums):
        print(symbol, end=" ")   
    print()
