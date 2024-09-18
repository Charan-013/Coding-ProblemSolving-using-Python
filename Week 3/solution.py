# TASK 1

value_1_int = 1 
print("initial value_1=", value_1_int)
value_1_int = 2 
print("changed value_1=", value_1_int)

value_2_float = 1.1
print("initial value_2=", value_2_float)

value_2_float = 2.2 
print("changed value_2=", value_2_float)

value_3_string = "MS"
print("initial value_3=", value_3_string)
 
print("changed value_3=", value_3_string + "IT")

#swap
a1 = 0
b1 = 100
print("Before swap a =",a1, ", b =",b1)
a1, b1 = b1, a1
print("After swap a =",a1, ", b =",b1)


print("--------------------------------------------")


# Task 2
var_integer = 1
var_float = 1.1
var_string = "MSIT"
var_boolean = True

print(type(var_integer), "Value =",var_integer)
print(type(var_float), "Value =",var_float)
print(type(var_string), "Value =",var_string)
print(type(var_boolean), "Value =",var_boolean)
print()
int_to_float = float(var_integer)
float_to_int = int(var_float)
float_to_string = str(var_float)
print("Integer to Float:", int_to_float)
print("Float to Integer:", float_to_int)
print("Float to String:", float_to_string)

print("--------------------------------------------")

# Task 3

var_integer = 1 # declaring int value 1 to var_integer. 
var_float = 1.1 # declaring float value 1.1 to var_float
var_string = "MSIT" #declaring string value MSIT to var_string
var_boolean = True #declaring boolean value true to var_string

print(var_integer) #printing value of var_integer
print(var_float) #printing value of value_float
print(var_string) #printing value of value_string
print(var_boolean) #printing value og var_boolean

print(var_integer1)
"""
output error:
Traceback (most recent call last):
  File "d:\MSIT\Python\Week 3\Task 3.py", line 11, in <module>
    print(var_integer1)
          ^^^^^^^^^^^^^^^^^
NameError: name 'var_integer1' is not defined.

The above error message is due to printing of undefined variable which is not initially declared in the program"""

print("--------------------------------------------")

# Task 4

print("MSIT"
# SyntaxError
# Explanation: this is because the print statement is missing a closing parenthesis so we are getting an error.

print(var)
# NameError
# Explanation: this is because the variable 'var' has not been defined or declared in the above code. and we are printing its value

int("MSIT")
# ValueError
# Explanation: Here string is declared insted of integer.

"string" + 5
#  TypeError
# Explanation: This error is because you cannot concatenate a string with an integer.Performing an invalid operation between incompatible data types

result = 5049 / 0
# ZeroDivisionError
# Explanation: this is because division by zero is not allowed in python programming.

import module
# ModuleNotFoundError:
# Explanation: this error is because we are trying to import a non-existent module in the installed python version
