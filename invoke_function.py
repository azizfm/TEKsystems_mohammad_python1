#import imp

from initialize_functions import *

'''
To use a function, you call it. When you call a function, you must provide values, or arguments, for each of the function’s parameters.
Functions allow you to write code efficiently. When you need to perform an action more than once, wrap that code in a function and call it when you need it. When you need to change how the action is carried out, you can change the code in the function, and the improvement is applied everywhere.
'''

print("Invoking zero arg function")
zero_arg_function()

print("Invoking function with required arguments")
introduction("Harry", "Houdini")

print("Invoking function with default arguments")
introduction_with_default_args()

#TODO: In this file, go ahead and invoke the rest of the functions from the initialize_functions.py file

print('Invoking function with mix of default argument')
introduction_with_mix_of_default_args('Aziz')

print('function that returns value')
product = product_of_two_num(5, 4)
print(product)

print()
print('function with the arbitrary arguments')
print(add_all_nums(2, 3, 4, 6))

print()
print("Doubleing the value of x")
print(double(8))

print()
print('Compute fibonacci sequence where the sum of the previous two numbers equals the current number.')
print(fib(1))
print(fib(2))
print(fib(3))
print(fib(4))
print(fib(5))
print(fib(10))
print(fib(15))
print(fib(20))


print()
print('subtracting two numbers by calling the subtract function')
print(subtract(1, 5))

print()
print('calling the function is_palindrome from initialize_function.py')
print(' to see if the string is a palindrome')
is_palindrome('bob')
print()
is_palindrome('jose')