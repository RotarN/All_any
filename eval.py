"""
eval(expression[, globals[, locals]]) executes a string containing Python code
				- single expression - and returns the result.
"""

x = 1
print(eval('x + 1'))


def perimeter(side_length):
	return 4 * side_length


def area(side_length):
	return side_length * side_length


def square_eval():
	expression = input("Type a function: ")
	if expression in ['perimeter', 'area']:
		for length in range(1, 6):
			result = eval(f'{expression}({length})')
			print(f"If side length is {length}, {expression.capitalize()} = {result}")
	else:
		print('Wrong Function')


# square_eval()


# TODO WARNING: Consider a situation when using a Unix system
#  (macOS, Linux etc) and the os module is imported.
#  The os module provides a portable way to use operating system functionalities like
#  reading or writing to a file. If users are allowed to input a value using eval(input()),
#  the user may issue commands to change file or even delete all the files
#  using the command: os.system('rm -rf *').

# 1. When both globals and locals parameters omitted
print(eval('dir()'))

# 2. Passing globals parameter; locals parameter is omitted
print(eval('dir()', {}))
print(eval('dir()', {'len': len, 'min': min}))

# 3. Passing both globals and locals dictionary
a = [1, 2]
print(eval('dir(a)', {'__builtins__': None}, {'a': a, 'dir': dir}))


from math import *
n = 169
scope_1 = eval('dir()')
print(scope_1)
scope_2 = eval('dir(n)', {'n': n, 'dir': dir})
print(scope_2)
