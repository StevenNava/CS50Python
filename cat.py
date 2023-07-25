# program that prints meow a given number of times
print('First print')
print('meow')
print('meow')
print('meow')

while True:
    numberOfMeows = int(input('Enter how many times you want this program to meow: '))
    if numberOfMeows > 0:
        break

# using a while loop
print('Second print')
i = 0
while i < numberOfMeows:
    print('meow')
    i += 1

# for loop
print('Third print')
for i in [0, 1, 2]:
    print('meow')

# for loop more pythonic -- use underscoe instead of i and use range
print('Fourth print')
for _ in range(numberOfMeows):
    print('meow')

# string multiplication print
print('Fifth print')
print('meow\n' * 3, end='')

def main():
    numberOfMeows = getMeowCount()
    printMeows(numberOfMeows)

def getMeowCount():
    while True:
        numberOfMeows = int(input('Enter how many times you want this program to meow: '))
        if numberOfMeows > 0:
            return numberOfMeows

def printMeows(numberOfMeows):
    for _ in range(numberOfMeows):
        print('meow')

main()