"""
all(iterable) returns True when all elements in a given iterable are true.
			If not, it returns False.
Equivalent to:
	def all(iterable):
		for element in iterable:
			if not element:
				return False
		return True

any(iterable) function accepts an iterable (e.g a list, dictionary, or tuple) as input and
			returns True if any element of the iterable is true. If not, it returns False.
Equivalent to:
	def any(iterable):
		for element in iterable:
			if element:
				return True
		return False
"""

boolean_list = ['True', 'True', 'True']
print(all(boolean_list))  # True
print(any(boolean_list))  # True

int_list = [1, 3, 4, 5]
print(all(int_list))  # True
print(any(int_list))  # True

mixed_list = [0, False]
print(all(mixed_list))  # False
print(any(mixed_list))  # False

# one false value
int_list = [1, 3, 4, 0]
print(all(int_list))  # False
print(any(int_list))  # True

# one true value
mixed_list = [0, False, 5]
print(all(mixed_list))
print(any(mixed_list))

# empty iterable
empty_list = []
print(all(empty_list))
print(any(empty_list))

empty_list = [[], ]
print(all(empty_list))
print(any(empty_list))

string = "This is a string"
print(all(string))
print(any(string))

dictionary = {0: 'False', 1: 'False'}
print(all(dictionary))
print(any(dictionary))

s = {1: 'True', 2: 'True'}
print(all(s))
print(any(s))
