# PySect

PySect is a Python learning project built to explore how Python objects behave at a lower level. It is designed to help you understand memory usage, reference counting, object allocation, container growth patterns, and bytecode execution using Python’s standard library modules such as `sys`, `gc`, `ctypes`, and `dis`.

This project is ideal for students and beginners who want to go beyond basic Python syntax and learn how Python actually works internally.

---

## What this project teaches

The program demonstrates a few important concepts:

- Object lifecycle and memory allocation
- Reference counting with `sys.getrefcount()`
- Memory footprint of built-in objects and custom classes
- Growth strategy of dynamic containers like lists and dictionaries
- Overhead comparison between different object types
- Python bytecode inspection using `dis.dis()`

In short, this project helps you answer questions like:

- How much memory does an object use?
- Why does a list grow in a certain way?
- What is the difference between a normal class and one using `__slots__`?
- What happens when Python creates or reuses objects internally?

---

## Project files

Inside the `pysect` folder you will find:

- `main.py` – the main executable script
- `exmple.py` – a supporting script with object-inspection experiments
- `README.md` – project documentation

---

## Prerequisites

Before running the project, make sure you have:

- Python 3 installed on your system
- A terminal or command prompt
- Access to the project folder

To check whether Python is installed:

```bash
python --version
```

If Python is installed correctly, you should see a version like `Python 3.x.x`.

---

## How to run the program

Open your terminal and navigate to the workspace root, then run:

```bash
cd "C:\Users\hp\Desktop\Practises-folder\Python\p"
python pysect/main.py
```

Or, from the project folder itself:

```bash
cd "C:\Users\hp\Desktop\Practises-folder\Python\p\pysect"
python main.py
```

Once it starts, the script shows a menu of test options.

---

## How to follow the instructions

The program asks for two things in sequence:

1. A menu number from 1 to 8.
2. A yes/no choice for whether you want to use a custom snippet or the built-in default examples.

Important: the first prompt expects a number, not `y` or `n`.

Example:

```text
 Enter test Choice >>> 5

 Do you want to enter custom snippet or test default(recommended) [y/n] >>> n
```

This means:

- `5` selects the container growth test
- `n` means use the built-in sample data, not a custom snippet

---

## Menu options explained

Here is what each menu option does:

### 1. Inspect object lifecycle
Shows information about an object such as:

- object memory address
- size in bytes
- reference count
- whether it is tracked by the garbage collector

This helps you understand how Python manages object lifetime.

### 2. Demonstrate reference count mutability
Shows how an object’s reference count changes when:

- it is passed into a function
- assigned to a new name
- stored in a container such as a list

### 3. Compare reference counts
Helps compare how different object references or containers affect reference count values.

### 4. Identify PyObject header overhead
Compares the size of basic Python objects such as:

- integers
- empty tuples
- empty lists
- empty dictionaries

This reveals how much metadata Python keeps around each object.

### 5. Inspect internal growth strategy of dynamic containers
Runs a test that repeatedly appends values to a list and reveals how list memory changes as it grows.

This is one of the most educational tests because it shows how Python manages list resizing.

### 6. Inspect memory footprint of dynamic container with key/value pairs
Compares memory usage between:

- dictionaries
- tuples of pairs
- normal class instances
- `__slots__` class instances

### 7. Evaluate the bytecode process of a function
Uses Python’s `dis` module to display the bytecode instructions of a function. This is useful for understanding how Python executes code underneath the syntax.

### 8. Run the full evaluation process
Runs the project’s combined post-processing flow and prints the main inspection reports together.

---

## Using the custom snippet option

If you choose `y` at the second prompt, the script asks for a code snippet and then uses `eval()` to evaluate it.

Example:

```text
 Enter test Choice >>> 1
 Do you want to enter custom snippet or test default(recommended) [y/n] >>> y
 Enter your code snippet to inspect lifecycle >>> [1, 2, 3, 4]
```

This will inspect the list `[1, 2, 3, 4]` and print its details.

Important notes:

- Use valid Python expressions.
- This is not a full multi-line script runner.
- For simple values and containers, it works very well.

Examples of valid snippets:

```python
[1, 2, 3]
{"name": "Festus", "age": 24}
("a", "b", "c")
```

---

## Suggested learning flow

To get the most value from this project, follow this order:

1. Run option 1 and look at object lifecycle output.
2. Run option 2 to understand reference counting.
3. Run option 4 to see object overhead.
4. Run option 5 to understand list growth behavior.
5. Run option 6 to compare container memory usage.
6. Run option 7 to inspect bytecode.
7. Finish with option 8 to see everything together.

This progression makes the project easier to understand because each step builds on the previous one.

---

## Example session

```bash
cd "C:\Users\hp\Desktop\Practises-folder\Python\p"
python pysect/main.py
```

Then:

```text
Actions that can be performed >>>

1. Inspect object lifecycle
2. Demonstrate reference count mutability
3. Compare reference counts
4. Identify PyObject header overhead
5. Inspect internal growth strategy of dynamic containers
6. Inspect Memory footprint of dynamic container with K,v pairs
7. Evaluate the excute bytecode process of a function

 Enter test Choice >>> 5
 Do you want to enter custom snippet or test default(recommended) [y/n] >>> n
```

---

## Notes

- This project is educational, not a polished production CLI.
- It uses Python’s built-in introspection features to help you learn lower-level behavior.
- It works best when you run one option at a time and read the output carefully.

The goal is not just to print numbers, but to understand what those numbers mean in Python’s memory model.

---

## Final tip

If you are learning Python seriously, try changing the sample values in `main.py` and running the program again. Small changes help you see how different objects affect memory, lifetime, and performance.

This project is a great beginner-to-intermediate exercise for understanding the Python runtime in a practical way.
