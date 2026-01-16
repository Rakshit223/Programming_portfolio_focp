This lecture focused on the fundamental concepts of variables and data types in Python, which are essential for writing meaningful and functional programs. It introduced how Python stores data using variables, how different data types behave, and how user input, functions, and collections such as lists are handled. Through practical exercises, students learned how Python dynamically assigns data types, manipulates values, and processes input and output efficiently. These concepts form the foundation for more advanced programming topics such as control structures, functions, and data structures 

Exercise-2 Variables and Types

KEY TECHNOLOGIES & CONCEPTS LEARNED:

Python Programming Language

Variables and Assignment

Primitive Data Types (int, float, string, boolean)

Dynamic Typing

Built-in Functions (print(), input(), type(), max(), len())

Augmented Assignment Operators (+=, *=)

String Handling and Escape Sequences

Lists and Mutability

Indexing and Slicing

User Input and Output

Type Conversion and Expressions




KEY NOTES:

A variable is used to store data values that can change during program execution.

Python uses dynamic typing, meaning the data type is determined at runtime based on the assigned value.

Common data types include:

Integer (int) – whole numbers

Float (float) – decimal numbers

String (str) – text data

Boolean (bool) – True or False

The type() function is used to check the data type of a variable.

The input() function always returns user input as a string, requiring type conversion for numerical operations.

Augmented assignment operators simplify updating variable values.

Strings support indexing and slicing, allowing access to specific characters or substrings.

Lists can store multiple values, including mixed data types, and are mutable, meaning their contents can be changed.

Strings are immutable, so they cannot be modified once created.

Built-in functions like max() behave differently depending on data type (e.g., comparing strings lexicographically).

Escape sequences (\n, \", \', \\) and triple-quoted strings help format complex text output.



EXTRA LEARNING RESOURCES:

Python Official Documentation – Data Types
https://docs.python.org/3/library/stdtypes.html

Python Official Tutorial – Variables
https://docs.python.org/3/tutorial/introduction.html

W3Schools Python Variables
https://www.w3schools.com/python/python_variables.asp


week3

This lecture explains how programs make decisions and repeat actions using control statements in Python. Earlier, programs only ran line by line, but this lecture shows how to add logic to programs. Students learned how to use conditions, loops, and Boolean expressions to control the flow of a program. These concepts help in writing real-world programs that can think, decide, and repeat tasks automatically 

3 Control Statements


K KEY TECHNOLOGIES AND CONCEPTS LEARNED :

Python control statements

Boolean expressions

Relational (comparison) operators

Logical operators (and, or, not)

Decision making using if, elif, else

Ternary operator

Looping using while and for

range() function

Membership testing (in, not in)

Loop control statements (break, continue)

Nested loops and nested conditions



KEY NOTES:

Programs work using sequence, selection, and iteration.

Boolean expressions always give True or False.

Comparison operators like <, >, ==, != are used in conditions.

The if statement checks a condition and runs code only if it is true.

else runs when the if condition is false.

elif is used to check multiple conditions.

Logical operators:

and → all conditions must be true

or → at least one condition must be true

not → reverses the result

Python allows chained comparisons, like 10 < x <= 50.

Membership testing checks if a value exists in a list or string.

Non-boolean values can also act as conditions:

0 or empty values → False

Non-zero or non-empty values → True

The ternary operator is a short form of if–else that returns a value.

while loop repeats as long as a condition is true.

for loop repeats over a sequence like a list or range.

range() generates numbers for loops.

break stops a loop immediately.

continue skips the current loop step and moves to the next one.

Loops and if statements can be nested inside each other.


EXTRA LEARNING RESOURCES:

Python If Statements – W3Schools
https://www.w3schools.com/python/python_conditions.asp

Python Boolean Expressions
https://www.programiz.com/python-programming/boolean

Python Loops – Programiz
https://www.programiz.com/python-programming/looping-technique

Python for Loop
https://www.w3schools.com/python/python_for_loops.asp

week4
This lecture explains how programs make decisions and repeat actions using control statements in Python. Earlier, programs only ran line by line, but this lecture shows how to add logic to programs. Students learned how to use conditions, loops, and Boolean expressions to control the flow of a program. These concepts help in writing real-world programs that can think, decide, and repeat tasks automatically 

3 Control Statements


K KEY TECHNOLOGIES AND CONCEPTS LEARNED :

Python control statements

Boolean expressions

Relational (comparison) operators

Logical operators (and, or, not)

Decision making using if, elif, else

Ternary operator

Looping using while and for

range() function

Membership testing (in, not in)

Loop control statements (break, continue)

Nested loops and nested conditions



KEY NOTES:

Programs work using sequence, selection, and iteration.

Boolean expressions always give True or False.

Comparison operators like <, >, ==, != are used in conditions.

The if statement checks a condition and runs code only if it is true.

else runs when the if condition is false.

elif is used to check multiple conditions.

Logical operators:

and → all conditions must be true

or → at least one condition must be true

not → reverses the result

Python allows chained comparisons, like 10 < x <= 50.

Membership testing checks if a value exists in a list or string.

Non-boolean values can also act as conditions:

0 or empty values → False

Non-zero or non-empty values → True

The ternary operator is a short form of if–else that returns a value.

while loop repeats as long as a condition is true.

for loop repeats over a sequence like a list or range.

range() generates numbers for loops.

break stops a loop immediately.

continue skips the current loop step and moves to the next one.

Loops and if statements can be nested inside each other.


EXTRA LEARNING RESOURCES:

Python If Statements – W3Schools
https://www.w3schools.com/python/python_conditions.asp

Python Boolean Expressions
https://www.programiz.com/python-programming/boolean

Python Loops – Programiz
https://www.programiz.com/python-programming/looping-technique

Python for Loop
https://www.w3schools.com/python/python_for_loops.asp

week 5

Python program files (*.py) can function as either scripts or modules, providing flexibility in code organization and execution (p. 18). Scripts are executed directly from the command line, while modules are imported into other programs for code reuse .



KEYNOTES:

Scripts vs. Modules: Working in interactive mode is good for small snippets, but substantial programs are stored in text files called scripts (p. 3). These files, with a .py suffix, can be executed by the Python interpreter (e.g., python my_program.py) (pp. 3-4). Any .py file containing definitions and statements can also be imported as a module into other programs.
Command Line Arguments: Arguments can be passed to a script upon execution and are accessed within the program via the sys.argv list (p. 5). The first element of sys.argv is the script's filename.
Importing:
Whole Module: import math creates a variable math in the local symbol table, and functions must be prefixed (e.g., math.sqrt(x)).
Aliasing: import math as m allows a shorter or different name to be used as a prefix (e.g., m.sqrt(x)).
Specific Elements: from math import sqrt, pi imports specific names directly into the local symbol table, requiring no prefix.
Wildcard Import: from math import * imports all content, but is generally discouraged due to potential name clashes.
Module Search Path: When a module is imported, Python checks for built-in modules first, then searches the directories listed in the sys.path variable (p. 13). This list is initialized to include the script's directory and the PYTHONPATH environment variable.
The __name__ Variable: The special __name__ variable allows a program to determine if it is being run as a script ("__main__") or imported as a module (its filename without the .py extension). This enables writing flexible code that can serve bothpurposes.
dir() Function: The built-in dir() function can be used in interactive mode to list all known names in the local symbol table, or all functions, types, and variables defined within an imported module.

RESOURCES WITH LINKS:

Official Python Documentation: The primary and most authoritative source for learning the language. The tutorial section is particularly useful for beginners and covers modules in depth.
Python 3.14.2 Documentation
The Python Tutorial (Modules section)

week6
List Manipulation: Exercises cover the use of list methods such as reverse(), append(), pop(), remove(), insert(), count(), and index().
Mutability: The document asks about the difference between mutable (lists) and immutable (tuples) data types, and how methods change them .
Accessors vs. Mutators: Questions require identifying whether specific methods are accessors (read-only) or mutators (changers).
List Comprehensions and Loops: There are tasks involving writing for loops to iterate over lists and creating lists using list comprehensions .
Tuple Operations: Exercises include creating, unpacking, indexing, and iterating over tuples, as well as the unique syntax for a single-element tuple.
Heterogeneous vs. Homogeneous: The final questions prompt the user to define "heterogeneous" in the context of tuples and the sister phrase for lists (homogeneous). 



KEY POINTS:

Mutability Distinction: The core concept is that Python lists are mutable (changeable after creation), while tuples are immutable (cannot be changed after creation).
Syntax: Lists are defined using square brackets [] and tuples use parentheses (). A single-element tuple requires a trailing comma, e.g., (1,).
List Methods: The exercises utilize methods that modify lists in-place (mutator methods), such as append(), extend(), insert(), remove(), pop(), reverse(), and sort().
Tuple Methods: Because tuples are immutable, they have fewer methods; the exercises focus on accessor methods that return information without changing the tuple, such as count() and index().
Accessors vs. Mutators: An accessor method reads a value (e.g., index()), while a mutator method changes the data structure (e.g., append()).
Iteration and Comprehension: Both lists and tuples can be iterated over using for loops, and lists can be generated concisely using list comprehensions.



RESOURCES:
For a deeper dive into these topics, the official Python documentation and other resources provide excellent, detailed information:
Official Python Tutorial (Data Structures): This is a primary source covering more on lists, list comprehensions, tuples, and sequences. It details all standard list methods.
Link: https://docs.python.org/3/tutorial/datastructures.html
Real Python: Lists vs. Tuples: A clear, beginner-friendly article that compares the key differences, use cases, and performance considerations.
Link: https://realpython.com/python-lists-tuples/
Google for Developers (Python Education): This page offers practical examples of common list methods append(), insert(), pop(), etc

week 7
Sets as Unordered Collections: Sets are unordered collections of unique elements; they do not support indexing or slicing because items have no fixed position.
Set Mutability: Regular sets (set()) are mutable data types, allowing elements to be added or removed (p. 2). A frozenset() is an immutable version .
Set Operations: Mathematical set operations covered include the & operator for intersection and the pipe | for union .
Set Comprehensions: Sets can be programmatically populated using comprehension syntax .
Dictionaries as Key-Value Pairs: Dictionaries store data as a mapping of unique keys to values, referred to as key-value pairs .
Dictionary Properties: Dictionaries are mutable, but their keys must be of an immutable type. Values do not need to be unique.
Accessing and Iterating Dictionaries: Values are accessed using square brackets with the corresponding key (e.g., stock["banana"]). Iteration can occur over keys or values using for loops.




KEY POINTS:

Sets as Unordered Collections: Sets are unordered collections of unique elements, which means they do not support indexing or slicing because items have no fixed position .
Set Mutability: Regular sets (set()) are mutable data types, allowing elements to be added or removed. A frozenset() is an immutable version that can be used where unchangeable data is required, such as in another set or as a dictionary key.
Set Operations & Operators: Mathematical set operations use specific operators, such as the & for intersection (common elements) or the pipe | for union (all elements).
Dictionaries as Key-Value Pairs: Dictionaries store data as a mapping of unique keys to values, a pairing often referred to as key-value pairs.
Dictionary Properties: Dictionaries are mutable, but their keys must be of an immutable type (like strings or numbers). Values do not need to be unique.
Accessing and Iterating Dictionaries: Values are accessed using square brackets with the corresponding key (e.g., stock["banana"]). Iteration can be done over.




RESOURECES WITH LINKS:

For a deeper dive into these topics, the official Python documentation and other resources provide excellent, detailed information:
Official Python Tutorial (Data Structures - Sets & Dicts): The core documentation covering operations and methods for both sets and dictionaries.
Link: docs.python.org
Real Python: Dictionaries in Python: A detailed guide on creating, accessing, and working with dictionaries.
Link: https://realpython.com/python-dicts/
W3Schools: Python Set Methods: A quick reference list of all built-in set methods and their shortcuts.
Link: www.w3schools.com

week 8

The section on string formatting emphasizes the use of Python's efficient f-strings (formatted string literals), which streamline the process of embedding variables and even expressions directly within string text. The exercises specifically task the user with applying various format specifiers using the colon : syntax to control output details, such as rounding floating-point numbers to specific decimal places (.2f), managing field width and alignment (:16.2f, ^), and specifying fill characters (:0>). Older formatting techniques, like the versatile str.format() method (which uses positional or keyword arguments) and the legacy % formatting style, are also introduced for comparison and potential maintenance of older codebases. String manipulation methods, such as str.rjust() for right-justifying text with padding, are explored through practical tasks like generating character patterns using loops.
The second major focus is on file handling, teaching the fundamental life cycle of interacting with external files. This includes using the vital open() function to acquire a file object and specifying the appropriate file mode (e.g., "r" for reading, "w" for writing, "b" for binary files). A core concept is the absolute necessity of calling the f.close() method to properly save data and release system resources. The exercises differentiate between various reading methods: f.read() for accessing the entire file content as one string, f.readline() for reading line by line, and f.readlines() for reading all lines into a list structure. The document also introduces methods for navigating within a file, such as f.tell() to determine the current cursor position and f.seek(0) to move that position back to the start. The best practice of using the with open(...) context manager is highlighted as a safer alternative to manual closing, as it guarantees file closure even if an error occurs. Finally, a common pitfall is identified: the f.write() method requires that all data be first converted into a string type before being written to a text file.




KEY POINTS:

String Formatting: Exercises utilize f-strings for embedding variables and expressions directly into strings, and touch upon older .format() and % formatting styles (pp. 2-3).
File Life Cycle: A file must be explicitly opened using the open() function and closed using the .close() method to ensure proper handling and prevent resource leaks (pp. 5, 7).
File Modes: Different modes are used for different operations, such as "r" for reading (the default), "w" for writing (overwrites), "a" for appending, and "b" for binary operations (pp. 5-6).
Reading Methods: The exercises cover f.read() (reads entire file), f.readline() (reads one line), and f.readlines() (reads all lines into a list) (p. 6).
File Pointer Control: Methods like tell() report the current file position, and seek(0) repositions the pointer to the beginning of the file (p. 7).
Context Managers: The with open(...) statement is highlighted as best practice because it automatically closes the file object upon exiting the block, even if an error occurs (p. 7).
Data Types for Writing: The f.write() method strictly requires a string argument; other data types must be converted first (p. 7).
Resources with Links
Since the user requested specific links, external resources from the previous search results are provided below. The provided PDF document itself does not contain any links (pp. 1-8).
Official Python Docs (Reading and Writing Files): Covers the essentials of file objects and methods like open(), read(), write(), and close().
Link: docs.python.org
Real Python: The with statement: Explains why with open(...) is the preferred and safer method for file handling.
Link: realpython.com
W3Schools: Python File Handling: Provides simple, executable examples for different file modes and methods.
Link: www.w3schools.com
PyFormat: An excellent guide to all types of string formatting in Python, including f-strings, .format(), and legacy % styles.
Link: pyformat.info
Would you like me to clarify how to implement one of these concepts, such as writing data to a file?



RESOURCES WITH LINKS:

Official Python Docs (Reading and Writing Files): Covers the essentials of file objects and methods like open(), read(), write(), and close().
Link: docs.python.org
Real Python: The with statement: Explains why with open(...) is the preferred and safer method for file handling.
Link: realpython.com
W3Schools: Python File Handling: Provides simple, executable examples for different file modes and methods.
Link: www.w3schools.com
