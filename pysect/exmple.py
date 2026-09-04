"""_summary_
we are building a program for 1 week that does a complex job

print(print("Hello world"));

UNDERSTAND THE COST OF EVERY SINGLE LINE YOU WRITE;
PySect (A CLI Python Runtime Diagnostic & Bytecode Inspector).

Build a lightweight command-line utility (using standard library only)
that accepts arbitrary Python code snippets or objects, analyzes their
underlying CPython mechanics, and prints a low-level diagnostic report.#
"""

import gc
import sys

"""
Objective:
- Object Allocator and lifecycle tracking.
- Track ref count and memory allocation using sys and gc modules.
- Disassemble and analyze bytecode using dis module.

"""

# print(gc.is_tracked(disassembler))
# print(id(disassembler))
# # print(gc.get_referrers(disassembler))
# print(f"\n {'=' * 40}\n Byte Test for the function Dissambler \n {'=' * 40} \n ")
# print(
#     f" final result: \n function size: {sys.getsizeof(disassembler)} bytes \n and ref count of: {sys.getrefcount(disassembler)} times"
# )

b = {}
a = {
    "times": [
        {
            "points": [
                {"roads": []},
                {"stores": []},
            ]
        },
        {
            "insttrument": [
                {
                    "organ": "keyboard",
                    "guitar": "strings",
                    "drums": [
                        {"electric": "vibes"},
                        {"hand": "noise"},
                    ],
                },
            ]
        },
    ]
}

# a = {}
# a.update({"name": "John", "age": 30, "city": "New York"})


def inspect_object(obj):
    print(f" {'=' * 40}\n INSPECTING OBJECT 1 \n {'=' * 40}")
    print("\n Memory address allocation analysis: \n ")
    print(hex(id(obj)))
    print("\n determining current reference count of object :")
    print(f"#{sys.getrefcount(obj)}")
    print("\n determining Size in bytes of object :")
    print(f"{sys.getsizeof(obj)} byte(s)")
    print("\nTracking Status :")
    print(gc.is_tracked(obj))
    print("\n Checking if finalised")
    print(gc.is_finalized(obj))
    print(obj)


# inspect_object(a)

# print(dis.dis(disassembler))
