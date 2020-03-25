## Create list with range
my_list = list(range(1, 10))
print(my_list)

my_list = list(range(1, 10, 2))
print(my_list)

print()

## Enumerate
words = 'abcdef'
for index, item in enumerate(words):
    print(f'{index}, {item}')

print()

## Zip
first_list = ['a', 'b', 'c', 'd', 'e']
second_list = [1, 2, 3]
third_list = [True, False, True, False]

for item in zip(first_list, second_list, third_list):
    print(item)

print()

## Create a list using zip
my_list = list(zip(first_list, second_list, third_list))
print(my_list)

print()

# in statement
print('a' in first_list)
print(4 in second_list)

print()

my_dict = {1: 'a', 2: 'b', 3: 'c'}
print(1 in my_dict)
print('a' in my_dict)
print('a' in my_dict.values())
print(1 in my_dict.keys())

print()

## min adn max
num_list = [10, 12, 9012, 1682, 3452, 283]

print(min(num_list))
print(max(num_list))

print()

## shuffle
from random import shuffle
new_num_list = [1, 2, 3, 4, 5, 6, 7, 8, 9]
shuffle(new_num_list)
print(new_num_list)

print()

## randint
from random import randint
print(randint(0, 100))
print(randint(100, 200))

print()

## input
name = input('Enter your Name: ')
print(name)
