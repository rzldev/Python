## List comprehension
my_string = 'Hello World!'
my_list = []

for letter in my_string:
    my_list.append(letter)

print(my_list)

my_new_list = [letter for letter in my_string]
print(my_new_list)

print()

num_list = [num for num in range(10)]
print(num_list)

num_list = [num**2 for num in range(10)]
print(num_list)

print()

num_list = [x for x in range(10) if x % 2 == 0]
print(num_list)

print()

celcius = [0, 12, 23, 34, 45, 56, 89, 100]
farenheit = [(9/5) * temp for temp in celcius]

print(farenheit)

print()

results = [x if x % 2 == 0 else 'ODD' for x in range(10)]
print(results)

print()

num_list = []
for x in [1, 2, 3]:
    for y in [400, 500, 600]:
        num_list.append(x*y)

print(num_list)

new_num_list = [x*y for x in [1, 2, 3] for y in [400, 500, 600]]
print(new_num_list)
