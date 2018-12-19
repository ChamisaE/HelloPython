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


pi_tuple = (3,1,4,1,5,9)

new_tuple = list(pi_tuple)
new_list = tuple(new_tuple)


super_villians = {'Fiddler' : 'Isaac Bowin', 'Captain Cold' : 'Lenord Snart'}

print(super_villians['Captain Cold'])


age = 21

if age > 16 :
    print('You are old enough to drive')
else :
    print('You are not old enough to drive')
elif age >= 21 :
    print('You are old enough to drive to drive a tractor trailer ')
else :
    print("you are not old enough to drive")