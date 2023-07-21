# def defines a custom function
#def hello(): # any arguments defined for a function would be put inside of the parentheses
#    print('Hello ', end='')

#name = input('What is your name? ')
#hello()
#print(name)

# in Python functions whitespace is used to determine where functions start/end after the def keyword
#def hello(name='World'): # default parameters can be set by using = and the default value inside the parentheses
#    print(f'Hello {name}')
#    # print('Hello', name) # could also print 'Hello name' this way

#name = input('What is your name? ')
#hello(name)
#hello() # will print 'Hello World'

# Python conventions have the main code at the top in a 'main' function and
# all supporting functions coming below it
def main():
    name = input('What is your name? ')
    hello(name)
    hello() # will print 'Hello World'

def hello(name='World'):
    print(f'Hello {name}')
    
main()

def main2():
    x = int(input('Enter a value for x: '))
    xSquared = sqr(x)
    print(f'The value of x squared is {xSquared}')
    #print('The value of x squared is',sqr(x)) # it could also be printed out this way

def sqr(x):
    return x * x # the return keyword returns a value from a function

main2()