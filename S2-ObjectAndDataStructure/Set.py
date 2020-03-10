## Create a sets
# set doesn't care about the order
# if there are index with the same value, it will only showed once
set1 = {'Computer', 'Laptop', 'Android', 'Laptop'}
print(set1)
print()

set2 = {'Speaker', 'Headset', 'Computer', 'Laptop'}
print('Laptop' in set2)
print(set1.intersection(set2))
print(set1.difference(set2))
print(set1.union(set2))

## Create an empty sets
empty_set = {}  # this is wrong
empty_set = set()
