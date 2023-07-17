"""
exec(object[, globals[, locals]]) executes dynamically the Python code block passed as
			a string or a code object, unlike eval() which can execute a single expression only.
			Returns None
"""
program = 'a = 5\nb=10\nprint("Sum =", a+b)'
exec(program)

exec('print(dir())', {})

globals_parameter = {'__builtins__': None}
locals_parameter = {'print': print, 'dir': dir}
exec('print(dir())', globals_parameter, locals_parameter)


# exec vs eval
def func(arg):
	print("Called with %d" % arg)
	return arg * 2


ret = exec('func(11)')
print(ret)
ret = eval('func(11)')
print(ret)


exec('for i in range(3): print(i)')

# Syntax Error for eval(): as it the argument is not an expression
# that can be evaluated but a for statement
# eval('for i in range(3): print(i)')

