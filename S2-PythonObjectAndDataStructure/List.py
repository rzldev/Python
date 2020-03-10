## Create a alphabets list
alphabets = ['A', 'B', 'C', 'D']

print(alphabets)
print()

## Count the length of the list
print(len(alphabets))
print()

## Print list value items by index number
print(alphabets[0])
print(alphabets[-1])
print(alphabets[:2])
print(alphabets[2:])
print()

## Add value to the list
alphabets.append('E')
print(alphabets)

alphabets.insert(0, 'F')
print(alphabets)

alphabets_extend = ['G', 'H', 'I']
alphabets.extend(alphabets_extend)
print(alphabets)

print()

## Remove value from the list
alphabets.remove("F")
print(alphabets)

alphabets_pop = alphabets.pop()
print(alphabets_pop)
print(alphabets)

print()

## Sort the list
alphabets.reverse()
print(alphabets)

alphabets.sort()
print(alphabets)

number = [4, 6, 2, 3, 8]

number.sort()
print(number)

number.sort(reverse=True)
print(number)

print()

## Create a new list with sorted values from other variable
sorted_number = sorted(number)
print(sorted_number)
print()

## Min, Max and Sum
print(min(number))
print(max(number))
print(sum(number))
print()

## Find the index of a value in the list
print(alphabets.index('C'))
print()

## Check if there is a value that we try to find
print("A" in alphabets)
print("Z" in alphabets)
print()

## Print item one by one in the list with looping
for index, item in enumerate(alphabets, start=1):  # item is name of a variable
    print(index, item)
print()

## Give seperate sign between the values in the list
alphabets_string = ' - '.join(alphabets)
print(alphabets_string)
print()

# making it back
alphabets_new = alphabets_string.split(' - ')
print(alphabets_new)
print()
