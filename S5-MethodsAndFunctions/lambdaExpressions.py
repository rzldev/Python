## map() >> returns a map object(which is an iterator) of the results
# after applying the given function to each item of a given iterable (list, tuple etc.)
def square(x):
    return x*x

my_nums = [1, 2, 3, 4, 5]
print(list(map(square, my_nums)))

def splicer(my_string) :
    if len(my_string) % 2 == 0 :
        return 'EVEN'
    else :
        return my_string[0]

names = ['Bruce', 'Clrak', 'Hal']
print(list(map(splicer, names)))

print()

## filter() >> filters the given sequence with the help of a function
# that tests each element in the sequence to be true or not.
def check_even(num):
    return num % 2 == 0

my_nums = [1, 2, 3, 4, 5]
print(list(filter(check_even, my_nums)))

print()

## lambda() >> function that can take any number of arguments,
# but can only have one expression.
my_nums = [1, 2, 3, 4, 5]
names = ['Bruce', 'Clrak', 'Hal']

new_square = lambda num: num**2
print(list(map(new_square, my_nums)))

print(list(map(lambda name: name[::-1], names)))
print(list(filter(lambda num: num % 2 == 0, my_nums)))
