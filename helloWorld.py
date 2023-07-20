name = input("What is your name? ") # Return values of input command is typed input - type string
                                    # single equals sign is the assignment operator
print("hello, " + name + "!")       # This is one way to add the variable to the print statment
print("hello,", name)               # The print function in Python takes in multiple arguments seperated by commas


# print(*objects, sep=' ', end='\n', file=sys.stdout, flush=False)
# The above is Python's documentation for the print function. It shows that it takes in
# and prints the objects with a single space as the seperator and ending in a newline character '\n'
# and also that it prints to the stdout display
# sep can be overridden to overwrite the seperator like so
print("hello, ", name, "!", sep='')
# end character can be overridden to change or remove it like so
print("hello, ", end='') # overriding ending character to remove newline
print(name, "!", sep='') # overriding seperator to remove space
# default values in python are shown with var=value in the function

#print("hello, ")
#print(name)
                                    # We can use string interpolation instead