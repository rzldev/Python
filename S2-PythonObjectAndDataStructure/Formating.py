# Create a dictionary
person = {'name' : 'Bob', 'age' : 25}

## Formatting string
sentence = '1. My name is ' + person['name'] + ', and i am ' + str(person['age']) + ' years old'
print(sentence)

# or
sentence = ' '
sentence = '2. My name is {}, and i am {} years old'.format(person['name'], person['age'])
print(sentence)

# or
sentence = ' '
sentence = '3. My name is {0}, and i am {1} years old'.format(person['name'], person['age'])
print(sentence)

# or
sentence = ' '
sentence = '4. My name is {0[name]}, and i am {0[age]} years old'.format(person)
print(sentence)

# or
sentence = ' '
person_info = ['Bob', 21]
sentence = '5. My name is {0[0]}, and i am {0[1]} years old'.format(person_info)
print(sentence)

# or
sentence = ' '
class Person():
    def __init__(self, name, age):
        self.name = name
        self.age = age

person1 = Person('Bob', 23)
sentence = '6. My name is {0.name}, and i am {0.age} years old'.format(person1)
print(sentence)

# or
sentence = ' '
sentence = '7. My name is {name}, and i am {age} years old'.format(name='Bob', age=26)
print(sentence)

# or
sentence = ' '
sentence = '8. My name is {name}, and i am {age} years old'.format(**person)
print(sentence)

# or
sentence = ' '
tag = 'h1'
text = 'This is a headline'
sentence = '<{0}>{1}</{0}>'.format(tag, text)
print(sentence)

print()

## Formatting integer
sentence = ' '
for i in range(1, 6):
    sentence = 'The value is {}'.format(i)
    print(sentence)

# or
sentence = ' '
for i in range(1, 6):
    sentence = 'The value is {:02}'.format(i)
    print(sentence)

print()

## Formatting decimal
sentence = ' '
pi =  3.14159265359
sentence = 'Pi is equal to {}'.format(pi)
print(sentence)

# or
sentence = ' '
pi =  3.14159265359
sentence1 = 'Pi is equal to {:.2f}'.format(pi)
sentence2 = 'Pi is equal to {:.3f}'.format(pi)
print(sentence1)
print(sentence2)

# or
sentence = ' '
sentence = '1 MB is equal to {:,}'.format(10**6)
print(sentence)

# or
sentence = ' '
sentence = '1 MB is equal to {:,.2f}'.format(10**6)
print(sentence)

print()

## Formatting datetime
# import datetime
import datetime
my_date = datetime.datetime(2019, 8, 8, 19, 18, 00)
print(my_date)

# or
sentence = ' '
sentence = '{:%B %d, %Y}'.format(my_date)
print(sentence)

# or
sentence = ' '
sentence = '{0:%B %d, %Y} fell on a {0:%A} and was the {0:%j} day of the year'.format(my_date)
print(sentence)

print()

## String formatting
first_name = 'Bob'
last_name = 'Walker'

sentence = "Hello, my name is {} {}".format(first_name, last_name)
print(sentence)

# or
sentence = f"Hello, my name is {first_name.upper()} {last_name.upper()}"
print(sentence)

print()

## String formatting
person = {'name' : 'Bob', 'age' : 25}

sentence = "My name is {}, and i'm {} years old".format(person['name'], person['age'])
print(sentence)

# or
sentence = f"My name is {person['name']}, and i'm {person['age']} years old"
print(sentence)

print()

## Integer formatting
calculating = "4 times 11 is equal to {}".format(4 * 11)
print(calculating)

calculating = f"4 times 11 is equal to {4 * 11}"
print(calculating)

print()

## Float formatting
pi = 3.14159265359

calculating = "pi is equal to {}".format(pi)
print(calculating)

calculating = f"pi is equal to {pi:.2f}"
print(calculating)

print()

## String formatting with loop
for index in range(1, 4) :
    sentence = "Number {}".format(index)
    print(sentence)

print()

for index in range(1, 4) :
    sentence = f"Number {index:02}"
    print(sentence)

print()

## Datetime formatting
import datetime
my_date = datetime.date(2019, 8, 16)
sentence = "{}". format(my_date)

print(sentence)

sentence = f"Today is {my_date:%B %d, %Y}"
print(sentence)
