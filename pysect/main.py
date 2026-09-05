"""_summary_
Building the lifecycle tracker
"""

import ctypes
import dis
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
    print(f" Feature {' ' * 20} value")
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


# test requirements


# 1. Write a function that continuously appends items to a
# list and measures sys.getsizeof() on each iteration to reveal
# CPython's array re-allocation growth pattern
class PyListObject(ctypes.Structure):
    _fields_ = [
        ("ob_refcnt", ctypes.c_ssize_t),
        ("ob_type", ctypes.c_void_p),
        ("ob_size", ctypes.c_ssize_t),
        ("ob_item", ctypes.POINTER(ctypes.c_void_p)),  # Direct array pointer
        ("allocated", ctypes.c_ssize_t),
    ]

def continous_append_test(container):
    print()
    print("=" * 60)
    print(
        f"\n INTERNAL GROWTH STRATEGY TEST for {container.__class__.__name__} \n {'_' * 60} \n"
    )
    print("=" * 60)
    print(
        f"\n Process {' ' * 5} Size (bytes) {' ' * 5}  Pointer ID {' ' * 10} Overhead (bytes) {' ' * 5} Reallocation?"
    )
    # determine reallocation pattern
    pattern = []
    addresses = []
    list_struct = PyListObject.from_address(id(container))
    # determine CPython bit to calculate offsets
    reallocated = False
    offset = 24 if sys.maxsize > 2**32 else 12
    for i in range(1, 21):
        # Extracts the direct pointer address to the contiguous items array previous instance
        array_addr = ctypes.cast(list_struct.ob_item, ctypes.c_void_p).value
        # determine previous instance size of object
        size = sys.getsizeof(container)

        container.append(i)

        # Extracts the direct pointer address to the contiguous items array next instance
        array_addr_after = ctypes.cast(list_struct.ob_item, ctypes.c_void_p).value
        # determine next instance size of object
        size_after = sys.getsizeof(container)

        # check if reallocation occured
        reallocated = array_addr != array_addr_after

        if size != size_after:
            pattern.append(size_after)

        address_of_i = hex(id(i))
        addresses.append(address_of_i)

        deep_size = get_deep_size(container)
        overhead = deep_size - size
        memory_address = hex(id(container))
        ref_count = sys.getrefcount(container)
        
        pointer_hex = hex(array_addr_after) if array_addr_after is not None else "0x0"

        print(
            f" Append #{i} {' ' * 5} {size} {' ' * 10}  #-- {pointer_hex} {' ' * 10} {overhead} {' ' * 10} {reallocated}"
        )
    return pattern


# test subjects
test_list = []
# Sample data
keys = ["name", "age", "role", "salary", "department"]
values = ["Festus", 24, "Frontend Engineer", 120000, "Engineering"]

# 1. Standard Dict
dict_obj = dict(zip(keys, values))

# 2. Tuple of key-value pairs
tuple_obj = tuple(zip(keys, values))


# 3. Standard Object with __dict__
class StandardClass:
    def __init__(self, k, v):
        for key, val in zip(k, v):
            setattr(self, key, val)


std_obj = StandardClass(keys, values)


# 4. Object using __slots__
class SlotsClass:
    __slots__ = ("age", "department", "name", "role", "salary")

    def __init__(self, k, v):
        for key, val in zip(k, v):
            setattr(self, key, val)


slots_obj = SlotsClass(keys, values)


def containers():
    result = continous_append_test(test_list)
    print()
    print("#" * 60)
    print(f"\n Memory addresses of appended items: {result} \n")


# Dict Overhead Profiler: Compare the memory footprint of a dict vs a
# tuple of key-value pairs vs __slots__ vs a standard object __dict__.


def compare_memory_footprint():
    dict_sz = get_deep_size(dict_obj)
    tupple = get_deep_size(tuple_obj)
    std = get_deep_size(std_obj)
    slots = get_deep_size(slots_obj)

    print(f"{'=' * 60} \n MEMORY FOOTPRINT OF OBJECT:  \n {'=' * 60}")
    print(f" dict object : {dict_sz}bytes")
    print(f" tupple object : {tupple}bytes")
    print(f" standard object : {std}bytes")
    print(f" slots object : {slots}bytes")
    compared_max = max(dict_sz, tupple, std, slots)
    print()
    print(f"Container with the Max Overhead: {compared_max} bytes")


"""_summary_
Bytecode & Stack Frame Engine (pysect.disassembler)

Goal: Analyze dynamic typing costs and opcode execution sequences using dis.
"""


def dissasssembler(func):
    print()
    print(f"{'=' * 60} \n BYTECODE AND STACK TRACE \n {'=' * 60}\n")
    print(f"LINE {' ' * 8} OPCODE {' ' * 18} STACK EFF")
    print("_" * 60)
    dis.dis(func)


# pysect
def pysect(func):
    dissasssembler(func)
    containers()
    lifecycle_tracker(func)


if __name__ == "__main__":
    print("Actions that can be performed >>> \n")
    print(" LIFECYCLE TESTING >>> \n")
    print("1. Inspect object lifecycle")
    print("2. Demonstrate reference count mutability")
    print("3. Compare reference counts")
    print("4. Identify PyObject header overhead")

    print("\n INTERNAL GROWTH STRATEGY TESTING >>> \n")
    print("5. Inspect internal growth strategy of dynamic containers")
    print("6. Inspect Memory footprint of dynamic container with K,v pairs")

    print("\n BYTE CODE AND STACK TRACING >>> \n")
    print("7. Evaluate the excute bytecode process of a function")

    print("\n POST PROCESS >>> SELECT 8")

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
        elif choice == 5:
            containers()
        elif choice == 6:
            compare_memory_footprint()
        elif choice == 7:
            dissasssembler(containers)
        elif choice == 8:
            print("-" * 80)
            print("|")
            print(f" \n | {' ' * 10} EVALUATING ALL INSPECTION PROCESS {' ' * 40} | \n")
            print("|")
            print("-" * 80)
            pysect(containers)
    else:
        print(" Invalid input. Please enter 'y' or 'n'.")
    print()
