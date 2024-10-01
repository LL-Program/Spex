
# Spe*
![Logo](Spe.png)
Spex (Spe*) is a modern interpreted programming language designed for clarity and ease of use. This README provides a comprehensive overview of the language, including commands, example code, and how to run your scripts.It was built for the CHIFEngine of the HTL class 1CHIF 2024.

## Table of Contents

1. [Getting Started](#getting-started)
2. [Example Code](#example-code)
3. [Running Spex Code](#running-spex-code)
4. [Commands and Their Descriptions](#commands-and-their-descriptions)
   - [include](#include)
   - [decl](#decl)
   - [declf](#declf)
   - [math](#math)
   - [print](#print)
   - [pyfunc](#pyfunc)
   - [access](#access)
   - [explode](#explode)
   - [del](#del)
   - [version](#version)
5. [Conclusion](#conclusion)

## Getting Started

To run Spex code, save your script with a .sx extension. You can run the code in Windows using the following command:

bash
./spex.exe filename.sx

## Example Code

Here is a simple example of Spex code that calculates the square root of a number, with command descriptions included within the code:
```


// Include necessary libraries or modules
include; // Allows the use of external libraries

// Declare a function named 'squareroot' that takes one argument 'x'
declf squareroot<x> {
    // Declare a float variable 'guess' initialized to 1.0
    decl float guess 1.0; // Initialize the guess for square root calculation

    // Iteratively improve the guess using the Babylonian method
    math guess (0.5 * ($guess + ($x / $guess))); // First iteration to improve guess
    math guess (0.5 * ($guess + ($x / $guess))); // Second iteration
    math guess (0.5 * ($guess + ($x / $guess))); // Third iteration
    math guess (0.5 * ($guess + ($x / $guess))); // Fourth iteration
    math guess (0.5 * ($guess + ($x / $guess))); // Fifth iteration
    math guess (0.5 * ($guess + ($x / $guess))); // Sixth iteration
    math guess (0.5 * ($guess + ($x / $guess))); // Seventh iteration
    math guess (0.5 * ($guess + ($x / $guess))); // Eighth iteration
    math guess (0.5 * ($guess + ($x / $guess))); // Ninth iteration
    math guess (0.5 * ($guess + ($x / $guess))); // Tenth iteration

    // Print the final result (the square root of x)
    print $guess; // Output the calculated square root
}

// Prints the Interpreted-Active-Functions using a python function to get it to work(for demonstration)
pyfunc print self.active_functions;

// Print a greeting message
print Hello!; // Output: Hello!

// Declare various types of variables
decl int name1 10; // Declare an integer variable
decl str name2 "esddfgv"; // Declare a string variable
decl float name3 10.1; // Declare a float variable
decl char name4 "e"; // Declare a character variable
decl bool name5 true; // Declare a boolean variable (true)
decl bool name6 false; // Declare a boolean variable (false)

// Access an object
access object name1; // Access the variable name1

// Clear memory
explode; // Clears the memory

// Delete a variable from memory
del name2; // Deletes the variable name2 from memory

// Print a greeting using a variable
print Hello $name4 !; // Output: Hello e!

// Version declaration
version 0.0.1; // Identifies that the code is written in version 0.0.1 and can only be executed in this version
```
## Commands and Their Descriptions
### include

Usage: include;

Allows the use of external libraries or modules in your code.

### decl

Usage: decl <type> <name> <value>;

Declares a variable of the specified type (int, str, float, char, bool) and initializes it with a value.

### declf

Usage: declf <function_name> <parameters> { ... }

Declares a function with the specified name and parameters. The code block within the curly braces defines the function's behavior.

### math

Usage: math <variable> (<expression>);

Description: Performs a mathematical operation and assigns the result to the specified variable.

### print

Usage: print <values>;

Outputs the specified values to the console.

### pyfunc

Usage: pyfunc <function_name> <parameters>;

Connects a Python function for specific functionality.

### access

Usage: access object <name>;
 
Accesses the specified object or variable.

### explode

Usage: explode;

Clears the memory, removing all declared variables.

### del

Usage: del <name>;

Deletes the specified variable from memory.

### version

Usage: version <version_number>;

Declares the version of the code, indicating which version of Spex it is compatible with.

## Run the Interpreter

 - Clone the project

- Windows:
```bash
  ./spex.exe filename
```

- Linux:

```bash
  pip install -r requirements.txt
  python linux.py filename
```
 - MacOS: 🤷 Why do you use MacOS for Coding???

## Contribute
 - Wenn du aus der 1CHIF bist gehe einfach auf den Discord Server!
 - [CHIFEngine Discord](https://discord.gg/KfNVQbYK)

Liste der Mitmachenden:

 - Lukas Rennhofer / @LL-Program
 - Moritz Rottensteiner / 
@Alyopolo


## Conclusion

Spex is a versatile programming language that supports a variety of data types and operations, making it suitable for various programming tasks. By understanding the commands and their usages, you can efficiently write and execute Spex code
