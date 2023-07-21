name = input('What is your name? ') # Return values of input command is typed input - type string
                                    # single equals sign is the assignment operator
print('hello, ' + name + '!')       # This is one way to add the variable to the print statment
print('hello,', name)               # The print function in Python takes in multiple arguments seperated by commas


# print(*objects, sep=' ', end='\n', file=sys.stdout, flush=False)
# The above is Python's documentation for the print function. It shows that it takes in
# and prints the objects with a single space as the seperator and ending in a newline character '\n'
# and also that it prints to the stdout display
# sep can be overridden to overwrite the seperator like so
print('hello, ', name, '!', sep='')
# end character can be overridden to change or remove it like so
print('hello, ', end='') # overriding ending character to remove newline
print(name, '!', sep='') # overriding seperator to remove space
# default values in python are shown with var=value in the function
# positional parameters passed into functions are not named and are ingested
# in the order they are passed
# named parameters are optional and are passed in at the end and are used/overridden by name

# Python can use either single or double quotes for strings -- just be consistent
# The escape character in Python is the '\' and is used for escape sequences \ characters
print('hello', '\'' + name + '\'' + '!') # this will surrond the name in single quotes

# f strings / format strings
print(f"hello, {name}!") # This uses format strings to insert the variable


# STRING METHODS FOR SANITIZING
name = name.strip() # This is essentially the 'trim' command and removes all whitespace around string
print(f'hello, {name}!')

name = name.capitalize() # This obviously capitalizes the first character of the string
print(f'hello, {name}!')

name = name.title() # This will capitalize the first character of each word
print(f'hello, {name}!')

# Functions can be chained if you want / need
name = name.strip().title()
# or even in the input before assigning to the variable
# name = input("What is your name? ").strip().title() # this will pass the input into strip and then that output 
                                                    # into the title function
