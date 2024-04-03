# Class 02 - Understanding Python Types and Error Handling

## Overview

In this lesson, we delve into Python's dynamic typing system, focusing on TypeError, type checking, type conversion, and error handling with `try-except` blocks, as well as utilizing `if` statements for flow control.

### TypeError

A `TypeError` occurs in Python when an operation or function is applied to an object of an inappropriate type. This can happen when you try to concatenate a string with a number, for instance.

### Type Check

Type checking is the process of verifying the type of an object at runtime. Python provides the `isinstance()` function to check an object's type against a specified type.

### Type Conversion

Type conversion, or type casting, involves converting an object from one data type to another. Common functions for type conversion include `int()`, `float()`, and `str()`, allowing for explicit data type changes.

### Try-Except

The `try-except` block in Python is used for exception handling, allowing the program to continue running even if an error occurs. It tries to execute the code in the `try` block, and if an error is encountered, it runs the code in the `except` block instead.

### If Statements

`If` statements are used for conditional execution. The code block under an `if` statement will execute if the condition is `True`. This is crucial for decision-making within your code based on specific conditions.

## Exercise

This exercise involves requesting user input for a name, salary, and bonus, then performing checks and conversions to ensure the data is of the correct type before calculating and displaying a final bonus and a simple Key Performance Indicator (KPI).

Remember to handle exceptions gracefully and provide feedback for invalid inputs, ensuring a robust application.

Happy coding!
