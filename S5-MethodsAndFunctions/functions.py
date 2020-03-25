## Create a function
def new_function():
    pass

print(new_function())

def hello_world():
    print('Hello World!')

hello_world()

print()

## Create a function that get some input to produse some output
def function1():
    return 'Hello World!'

print(function1())
print(function1().upper())

print()

## Create a function with arguments
def greeting(name):
    return f'Hello {name}!'

print(greeting('Bob'))

def new_greeting(my_name, my_greeting='Hi'):
    return f'{my_greeting}, {my_name}!'

print(new_greeting('Tom'))

print()

## Create a function with limitless argument with (*) sign
## and add additional argument with (**) sign

# *args
def args_func(*args):
    return sum(args)

print(args_func(32, 92, 48, 182, 2))

print()

# *kwargs
def kwargs_func(**kwargs):
    if 'fruit' in kwargs:
        return ('My fruit of choice is {}'.format(kwargs['fruit']))
    else :
        return 'I did not find any fruit here'

print(kwargs_func(fruit = 'apple', name = 'john', veggie = 'lettuce'))

print()

# using args and kwargs
def student_info(*args, **kwargs):
    print(args)
    print(kwargs)

student_info('Bob', 'Student', '23', study='Math')

student = ['Bob', 'Student', '23']
courses = {'study': 'Math'}

student_info(student, courses)
student_info(*student, **courses)

print()

## Create a nested function
month_days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

def year_leap(year):
    return year % 4 == 0 and (year % 100 != 0 or year % 400 == 0)

def days_in_month(year, month):
    month -= 1
    if year_leap(year) and (month >= 0 and month <= 11):
        month_days[1] = 29
        return month_days[month]
    elif month >= 0 and month <= 11:
        return month_days[month]
    else:
        return "Invalid Month!"

print(year_leap(2020))
print(days_in_month(2020, 13))
