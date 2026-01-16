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