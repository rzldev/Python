## Create a variable with string value
message = 'Hello World!'

## Print variable message
print(message)
print()

## Using single quotes and double quotes
single = 'He said "Hello World!"'
double = "You're coding right now"
print(single)
print(double)
print()

## Using triple quotes
triple = """You are trying to learn
about quotes on python"""
print(triple)
print()

## Count the length of the string value
print(len(message))
print()

## Access some index of thestring value
print(message[0])
print(message[0:5])
print(message[6:11])
print()

# other way
print(message[:5])
print(message[6:])
print()

## Print string value with lowercase and uppercase
print(message.lower())
print(message.upper())
print()

## Count some index in the string value
print(message.count('Hello'))
print(message.count('l'))
print()

## Find some index in the string value
print(message.find('World'))
print(message.find('Universe'))
print()

## Replace string value
message = message.replace('World', 'Universe')
print(message)
print()

## Combine two string value
hello = 'Hello'
name = 'John'
greeting = hello + ', ' + name + '. Welcome to the party!'
print(greeting)

# second way
greeting = '{}, {}. Welcome to the party!'.format(hello, name)
print(greeting)

# third way
greeting = f"{hello}, {name}. Welcome to the party!"
print(greeting)
print()

## Check all of the atributs and method on the string value (Remove the "#" sign)
print(dir(greeting))
print()

# and to check the information for the string (Remove the "#" sign)
print(help(str))
print(help(str.lower))
print()
