# modulo
#number = int(input('Enter a number: '))

#if number % 2 == 0:
#    print(f'{number} is even!')
#else:
#    print(f'{number} is odd!')

# function for even or odd
def main():
    number = int(input('Enter a number: '))
    print(f'The number {number} is {determineEvenOrOdd(number)}!')

def determineEvenOrOdd(number):
    if number % 2 == 0:
        return 'even'
    else:
        return 'odd'
 
main()

def main2():
    number = int(input('Enter a number: '))
    if isEven(number):
        print(f'The number {number} is even!')
    else:
        print(f'The number {number} is odd!')

def isEven(number):
    if number % 2 == 0:
        return True
    else:
        return False
    # this can also be written in Python like this:
    # return True if number % 2 == 0 else False

    # this however is better/more succint and readable
    # return number % 2 == 0

main2()