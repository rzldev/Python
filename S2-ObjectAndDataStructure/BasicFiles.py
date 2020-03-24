## Open a file
my_file = open('public/myfile.txt')

## Read content inside the file
print(my_file.read())

print()

## Reset rhe cursor
print(my_file.read())
my_file.seek(0)
content = my_file.read()
print(content)

## Read content inside the file by the lines
my_file.seek(0)
print(my_file.readlines())

print()

## Close files
my_file.close()

## Open file using with statement
with open('public/myfile.txt') as f :
    print(f.read())

## Mode that can used when opening files
# r = read only
# w = write only(overwrite the file or create new one)
# a = append only(add new line to the file)
# r+ = reading and writing
# w+ = reading and writing(overwrite the file or create new one)

## r
with open('public/new_file.txt', 'r') as f :
    print(f.read())

print()

## a
with open('public/new_file.txt', 'a') as f :
    f.write("I can add a new line")

with open('public/new_file.txt', 'r') as f :
    print(f.read())

print()

## w
with open('public/created_file.txt', 'w') as f :
    f.write("This is my new file")

with open('public/created_file.txt', 'r') as f :
    print(f.read())
