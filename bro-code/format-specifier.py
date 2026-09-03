
# Format specifiers in py
# {:flags} this formats a value based on what flags are inserted

price1 = 300.58585
price2 = 485.48994
price3 = 3897.397487

# .(number)f to round to that many decimal places eg
print(f"prices are {price1:.2f}")
print(f"prices are {price2:.2f}")
print(f"prices are {price3:.2f}")

# :(number) allocate that many spaces
print(f"prices are {price1:10}")
print(f"prices are {price2:10}")
print(f"prices are {price3:10}")

# :03 allocate and zero pad that many spaces
# this would indictae the number of spaces gap left to be filled by zero
print(f"prices are {price1:020}")
print(f"prices are {price2:020}")
print(f"prices are {price3:020}")

# :< left justify
print(f"prices are {price1:<10}")
print(f"prices are {price2:<10}")
print(f"prices are {price3:<10}")

# :> right justify
print(f"prices are {price1:>10}")
print(f"prices are {price2:>10}")
print(f"prices are {price3:>10}")

# :^ center align
print(f"prices are {price1:^10}")
print(f"prices are {price2:^10}")
print(f"prices are {price3:^10}")

# :+ use a plus sign to indicate positive value 
print(f"prices are {price1:+}")
print(f"prices are {price2:+}")
print(f"prices are {price3:+}")

# := place sign to leftmost position
print(f"prices are {price1:=}")
print(f"prices are {price2:=}")
print(f"prices are {price3:=}")

# : insert a space before positive numbers 
print(f"prices are {price1:}")
print(f"prices are {price2:}")
print(f"prices are {price3:}")

# :, comma separatr # 
print(f"prices are {price1:,}")
print(f"prices are {price2:,}")
print(f"prices are {price3:,}")

# they do not need be writen so idle the format specifiers could be mixed to achieve a certain 
# aim at ones 
print(f"prices are {price1:+015,.3f}")
print(f"prices are {price2:+015,.3f}")
print(f"prices are {price3:+015,.3f}")
# this match will also work well
