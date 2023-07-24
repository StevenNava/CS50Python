# match statement which is comparable to the switch statment
name = input('What is your name? ')
#if name == 'Harry' or name == 'Ron' or name == 'Hermoine':
#    print('You are in Gryffindor!')
#elif name == 'Draco':
#    print('You are in Syltherin!')
#else:
#    print('You are in Hufflepuff!')

match name:
    case 'Harry' | 'Ron' | 'Hermoine': # this is one '|' or the other '|' or the other
        print('You are in Gryffindor!')
    case 'Crab' | 'Goyle' | 'Draco':
        print('You are in Slytherin!')
    case _: # this stands for anything not addressed in the previous cases
        print('You are in Hufflepuff!')