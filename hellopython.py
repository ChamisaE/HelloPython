import random
import sys
import os

print("Hello World")


#comment

'''
Multiline comment
'''

name = "Derek"
print(name)
name = 15
'''
Main datatypes: numbers stirngs lists tuples dictionaries

main math functions: + - * / % **exponential //floor division, rounds down
pay attention to order of operations
'''

print("5 + 2 = ", 5+2)
print("5 - 2 =", 5-2)
print("5 * 2 =", 5*2)
print("5 % 2 =", 5%2)
print("5 ** 2 =", 5**2)
print("5 // 2 =", 5//2)

quote = "\"Always remember you are unique"

multi_line_quote = ''' just like everyone else'''

new_string = quote + multi_line_quote

print("%s %s %s" %('I like the quote', quote, multi_line_quote))

print('\n' * 5)
