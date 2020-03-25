## Create a loop using while statements
x = 0

while x < 10:
    print(x)
    x += 1

print()

x = 1

while x <= 10:
    print(x)
    x += 1

print()

## Create an infonite loop with some conditional
y = 0

while True:
    if y == 10:
        print('Stopped!')
        break
    print(y)
    y += 1
