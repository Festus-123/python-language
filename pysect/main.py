"""_summary_
Building the lifecycle tracker
"""

import gc
import sys


# functions to eterminse size and overhead cost of object in memory
def get_deep_size(obj, seen=None):
    """Recursively finds size of objects"""

    size = sys.getsizeof(obj)

    if seen is None:
        seen = set()

    obj_id = id(obj)
    if obj_id in seen:
        return 0

    # Mark as seen
    seen.add(obj_id)

    if isinstance(obj, dict):
        size += sum(
            [get_deep_size(v, seen) + get_deep_size(k, seen) for k, v in obj.items()]
        )
    elif isinstance(obj, (list, tuple, set, frozenset)):
        size += sum([get_deep_size(i, seen) for i in obj])
    elif hasattr(obj, "__dict__"):
        size += get_deep_size(obj.__dict__, seen)
    elif hasattr(obj, "__iter__") and not isinstance(obj, (str, bytes, bytearray)):
        size += sum([get_deep_size(i, seen) for i in obj])
    return size


# function lifecycle tracker
def lifecycle_tracker(obj):
    print(
        f" {'=' * 50} \n DIAGNOSTIC REPORT OF {obj.__class__.__name__} \n {'=' * 50} \n "
    )

    print(" [1.] Object Lifecycle >>> \n")
    print("<<< Memory address allocation analysis >>>\n")
    print(f" Memory address in RAM: {' ' * 20} {hex(id(obj))} \n")
    print("#" * 50)
    print("\n <<< Deep size analysis >>> \n")
    print(f" Feature {' ' * 40} value")
    print("_" * 50)
    print(f" Shell or container size {' ' * 12} {sys.getsizeof(obj)} bytes")
    print(f" Total size (internal data) {' ' * 10} {get_deep_size(obj)} bytes")
    print(
        f" Overhead cost {' ' * 20} {get_deep_size(obj) - sys.getsizeof(obj)} bytes \n"
    )
    print("#" * 50)
    print("\n <<< Reference count analysis >>> \n")
    print(f" Reference count: {' ' * 20} #{sys.getrefcount(obj)} \n")
    print("#" * 50)
    print("\n <<< Tracking status analysis >>>\n")
    print(f" Tracking status: {' ' * 20} {gc.is_tracked(obj)} \n")
    print("#" * 50)
    print()


# test objects and containers as well
# --- Test Bench ---

# 1. Simple Flat List
flat_list = [1, 2, 3, 4, 5]

# 2. Nested Dictionary with mixed data types
complex_dict = {
    "user": "Festus",
    "roles": ["Admin", "Developer"],
    "metadata": {"session_id": 98412, "active": True},
}


# 3. Custom Class Instance
class InventoryItem:
    def __init__(self, name, qty):
        self.name = name
        self.qty = qty
        self.tags = ["hardware", "storage"]


item = InventoryItem("NVMe SSD", 15)

"""_summary_
    Demonstrate reference count mutability: Create a test harness 
    showing how passing an object to functions, binding it to new names, 
    or appending it to lists mutates its refcount in real time.
"""

# creating a text harness to demonstrate reference count mutability


# 1. passing an object to a function
def receive_obj(obj):
    print(f" {'=' * 50} \n RECEIVING OBJECTS TEST HARNESS \n {'=' * 50} \n ")
    print(f" Type {' ' * 5} ref_count {' ' * 5} memory_address {' ' * 5} is_tracked")
    print("_" * 50)
    print(
        f" {obj.__class__.__name__} {' ' * 5} {sys.getrefcount(obj)} {' ' * 5} {hex(id(obj))} {' ' * 5} {gc.is_tracked(obj)} \n"
    )


# 2. binding it to a new name
new_name = flat_list

# 3. appending it to a list
list_container = []
list_container.append(flat_list)


def get_ref_count(obj):
    print(f" {'=' * 50} \n ref count test 2 and 3 \n {'=' * 50} \n ")
    print(f" type {' ' * 5} ref_count {' ' * 5}")
    print("_" * 50)
    print(f" {obj.__class__.__name__} {' ' * 5} {sys.getrefcount(obj)} \n")


"""_summary_
    Identify PyObject header overhead: Compare sys.getsizeof across integers, 
    empty tuples, empty lists, and empty dicts to map fixed CStruct header costs.
"""
# integers
int_obj = 42

# empty tuples
empty_tuple = ()

# empty lists
empty_list = []

# empty dicts
empty_dict = {}


def compare_header_overhead(obj):
    print(f" {'=' * 50} \n Header Overhead Comparison \n {'=' * 50} \n ")
    print(f" Type {' ' * 20} Size (bytes)")
    print("_" * 50)
    print(f" {obj.__class__.__name__} {' ' * 20} {sys.getsizeof(obj)} \n")
    print()
    max_header = max(
        sys.getsizeof(int_obj),
        sys.getsizeof(empty_tuple),
        sys.getsizeof(empty_list),
        sys.getsizeof(empty_dict),
    )
    print(f"\n MAXIMUM HEADER OVERHEAD: {max_header} bytes \n")
    print("#" * 50)
    print()


"""_summary_
    2. Goal: Expose the internal growth strategies and memory footprints 
       of dynamic containers (list vs dict vs tuple vs set).
"""


def containers(con):
    print()


# test requirements

# 1. Write a function that continuously appends items to a
# list and measures sys.getsizeof() on each iteration to reveal
# CPython's array re-allocation growth pattern


def continous_append_test():
    test_list = []
    for i in range(1, 21):
        test_list.append(i)
        print()
    return test_list 


if __name__ == "__main__":
    print("Actions that can be performed >>> \n")
    print("1. Inspect object lifecycle")
    print("2. Demonstrate reference count mutability")
    print("3. Compare reference counts")
    print("4. Identify PyObject header overhead")

    choice = int(input("\n Enter test Choice >>> "))
    snippet_format = input(
        "\n Do you want to enter custom snippet or test default(recommended) [y/n] >>> "
    )

    if snippet_format.lower() == "y":
        snippet = input("\n Enter your code snippet to inspect lifecycle >>> ")
        custom_snippet = eval(snippet)
        if choice == 1:
            lifecycle_tracker(custom_snippet)
        elif choice == 2:
            receive_obj(custom_snippet)
        elif choice == 3:
            get_ref_count(custom_snippet)
        elif choice == 4:
            compare_header_overhead(custom_snippet)
    elif snippet_format.lower() == "n":
        if choice == 1:
            lifecycle_tracker(flat_list)
            lifecycle_tracker(complex_dict)
            lifecycle_tracker(item)
        elif choice == 2:
            receive_obj(flat_list)
            receive_obj(complex_dict)
            receive_obj(item)
        elif choice == 3:
            get_ref_count(new_name)
            get_ref_count(list_container)
        elif choice == 4:
            compare_header_overhead(int_obj)
            compare_header_overhead(empty_tuple)
            compare_header_overhead(empty_list)
            compare_header_overhead(empty_dict)
    else:
        print(" Invalid input. Please enter 'y' or 'n'.")
    print()
