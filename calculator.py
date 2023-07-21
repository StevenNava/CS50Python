x = 1
y = 2 
z = x + y
print(z)

x = input('Enter a value for x: ')
y = input('Enter a value for y: ')
z = x + y
print(z)
# the above doesn't work because input takes the values entered in as string types
# so when it is supposed to add them it instead concatenates them

z = int(x) + int(y) # you can cast the strint to an int by using the fucntion int()
print(f'Integer value for z is: {z}')
print(f'Integer value for z is: {int(x) + int(y)}') # you can enter statements inside of the print(f'') to be calculated


x = int(input('Enter a value for x: ')) # you can cast the result of an input statement like so, passing the value into the int function
y = int(input('Enter a value for y: '))
print(f'x + y = {x + y}') 

x = float(input('Enter a decimal value for x: '))
y = float(input('Enter a decimal value for y: '))
print(f'x + y = {x + y}') 

z = round(x + y) # round rounds the number to the specified number of decimal places round(number[, ndigits])
print(f'The rounded result of x + y is: {z}')
print('We are going to take the output value and multiply it by 1000 to get a larger number.')
z = z * 1000
print(f'The larger number is: {z:,}') # this will add commas to larger numbers that need them formatting the string

print('Round can be used to round strings to a given decimal place. Here is an example of rounding 2/3.')
print(f'2/3 rounded to the hundredths place is: {round(2/3, 2)}')
# the same problem can be solved using f strings like so
print(f'2/3 rounded to the hundredths place is: {(2/3):.2f}')