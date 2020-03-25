## Using a loop statements
nums = [1, 2, 3, 4, 5]

for num in nums:
    print(num)

print()

## Use break to stop the looping with some conditional
for num in nums:
    if num == 3:
        print('Found!')
        break
    print(num)

print()

for num in nums:
    print(num)
    if num == 3:
        print('Start!')
        break

print()

## Use continue to skip the looping with some conditional
for num in nums:
    if num == 3:
        print('Skipped!')
        continue
    print(num)

print()

for num in nums:
    print(num)
    if num == 3:
        print('It won\'t do anything!')
        continue

print()

## Create a nested loops
for num in nums:
    for letter in 'abc':
        print(num, letter)

print()

## Create loops with a range
for i in range(10):
    print(i)

print()

for i in range(1, 11):
    print(i)

print()

for i in range(1, 11, 3):
    print(i)

print()
