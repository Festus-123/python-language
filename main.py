# print(print("Hello world"));

# UNDERSTAND THE COST OF EVERY SINGLE LINE YOU WRITE;

# PySect (A CLI Python Runtime Diagnostic & Bytecode Inspector).
#
# Build a lightweight command-line utility (using standard library only)
# that accepts arbitrary Python code snippets or objects, analyzes their
# underlying CPython mechanics, and prints a low-level diagnostic report.#
#
import sys

# print(dir(sys))

data = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
item = iter(data)
data.append(14)
size = sys.getsizeof(data)
ref_count = sys.getrefcount(data)

# print(sys.__dict__.keys());
# print(f'{"=" * 40} \n PROJECT OVERVIEW \n {"=" * 40} \n \n Value and Size: \n {size} bytes \n\n Ref Count (optional changes or shifts): \n {ref_count} times')

# life cycle
# containers
# disassembler#


def lifecycle():
    print("*** User personal data ***  \n")
    name = input("Enter your name >>> ")
    age = int(input("Enter your age >>> "))
    print(f"\n Your name is {name} and your age is {age}years \n saved succesfully! \n")
    print("*" * 30)
    print(f" \n Good Morning to you {name}! \n")
    print("*" * 30)
    print("It is hot out there today you might want to take a break")
    print(" is there any thing else you want to let me know about you?? \n")
    print("i could suggest a few if you want >>>")
    print("\n 1. your schools... ?")
    print("\n 2. your Friends... ?")
    print("\n 3. your hobbies... ?")
    choice = int(input("Enter your choice >>>"))
    if choice == 1:
        print("*" * 30)
        print("I love Eduction... where do we start from")
        print("*" * 30)
    elif choice == 2:
        msg = "Oohh this is gonna be interesting... am kind of a lonner 😓 other than you i have no friends"
        print("*" * len(msg))
        print(msg)
        print("*" * len(msg))
    elif choice == 3:
        print("*" * 30)
        print("Hobbiess... have got a few myself wanna see?")
        print("*" * 30)

    return {name, age}


def disassembler():
    print("\n *** Hi There i am your Agetic Ai Moged ***")
    print("\n <<< What would you like to do today? >>> ")
    print(" \n 1. Get to know you?")
    print(" \n 2. Chat with you?")
    print(" \n 3. Answwer some basic questions?")

    choice = int(input("\n select a number >>> "))

    if choice == 1:
        lifecycle()

    print("program terminated")


# disassembler()
