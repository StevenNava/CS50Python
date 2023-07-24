score = int(input('Enter your grade: '))

# and syntax
if score >= 90 and score <= 100:
    print(f'Your grade of {score} gets you an A!')
elif score >= 80 and score < 90:
    print(f'Your grade of {score} gets you a B!')
elif score >= 70 and score < 80:
    print(f'Your grade of {score} gets you a C!')
elif score >= 60 and score < 70:
    print(f'Your grade of {score} gets you a D!')
else:
    print(f'Your grade of {score} gets you a F!')

# Pythonic syntax
# By switching the comparison in python we can chain comparisons to improve readability
if 90 <= score <= 100:
    print(f'Your grade of {score} gets you an A!')
elif 80 <= score < 90:
    print(f'Your grade of {score} gets you a B!')
elif 70 <= score < 80:
    print(f'Your grade of {score} gets you a C!')
elif 60 <= score < 70:
    print(f'Your grade of {score} gets you a D!')
else:
    print(f'Your grade of {score} gets you a F!')

if score >= 90:
    print(f'Your grade of {score} gets you an A!')
elif score >= 80:
    print(f'Your grade of {score} gets you a B!')
elif score >= 70:
    print(f'Your grade of {score} gets you a C!')
elif score >= 60:
    print(f'Your grade of {score} gets you a D!')
else:
    print(f'Your grade of {score} gets you a F!')