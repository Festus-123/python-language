# collections in py
# single "variale" used to store multiple vlues 
# list [] it is ordered and changeable, Duplicates ok
# set {} unordered and immutable, but add/remove Ok, No Duplicates
# tupple ()  ordered and unchangeable, Duplicates OK  #

# a list


fruits = ["apple", "banana", "orange"]
print(fruits)
print(fruits[1], fruits[2]) 
# accessing n eleement found in the list
# if we enter an index that is within rage will return an index error
# we could use the start end and step methodwithin the index as well #

print(fruits[0:3]) # with steps any of your pattern 

# we could iterate iver collection with a forloop

for fruit in fruits:
    print(fruit)

# metod used with collection
# print(dir(fruits))
#  for full description we use 
# print(help(fruits))

# we also have lenght method 
# print(len(fruits))

# the in method or operator checksif a value is within a colelction
# print("apple" in fruits)

# we could chaneg value after we create our list

# fruits[0] = "biscuit"
# print(fruits)

#  we ould append an elemen i.e ads a element to the end of a list 
fruits.append("bicycle")
print(fruits)

# we could also use the remove method to rremove anelement from a list
fruits.remove("apple")
print(fruits)

# using insert method we can insert a value at a given index
fruits.insert(1, "cocnut")
print(fruits)

# sort method wll sort a list alphabetically
fruits.sort()
print(fruits)

# the reverse method reverse a list not alphabetically but basedon how they are arrnged...
fruits.reverse()
print(fruits)

# # we can clear a list using the clear method 
# fruits.clear()
# print(fruits)

# wean return the index of a value 
print(fruits.index("bicycle")) # if a value dosen't exist and we try gtting the index it retuen index error 

# since duplicate are permitted in list we can sount the numebr of occurence of s value
print(fruits.count("bicycle"))




#  justlike list a set is a colecton
# except that it dosen't allows dupplicates and it is immutable and unordered 
# the arrangment canges each time it is printed #

vegetables ={"apple", "banna", "ornage", "ciggarrreeetee", "womeennn"}
print(vegetables)

#  the method that applied in list also apply to set just with a little limit and restrain 
#  especially in terms of dupplicate 
#  also the dir(vegetables help ) so as the help(vegetable for description)

# in set er use the 
# len()
# in
# for
# 
# but he index can't be applied since set s unordered 
# remove
# add
# 
# we an't change the value of a set (immutable)
# pop random
# push random
# clear
# set orks well when working with cnstants  #



# Tupple
# this are ordered and unchangeable but duppliates are permited 
# tupple are faster than list  #

foods = ("rice", "beans", "yam", "semovita")
print(foods)


# methods that works well with tupple

# dir() help()
# in
# len()
# indexing also works cause it is ordered index[]
# count
# for
# and other methods  #