x = int(input('Enter a value for x: '))
y = int(input('Enter a value for y: '))

# if and elif is the is / else if syntax -- else can also be used
if x > y:
    print(f'{x} is greater than {y}!')
elif x < y:
    print(f'{x} is less than {y}!')
else:
    print(f'{x} equals {y}!')

# or syntax
if x > y or x < y:
    print(f'{x} is not equal to {y}!')
else:
    print(f'Once again {x} is equal to {y}!')

if x != y:
    print(f'{x} is not equal to {y}!')
else:
    print(f'Once again {x} is equal to {y}!')