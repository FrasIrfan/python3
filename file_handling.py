# Write mode
file = open("example.txt", "w")
file.write("Line no 1\n")
file.write("Line no 2")


file = open("example.txt", "w")
for i in range(1,101):
    file.write(f"Line no {i}\n")
    # An f-string, also known as a formatted string literal,
    # is a feature introduced in Python 3 that allows you to embed
    # expressions inside string literals, using curly braces {}.

# Append Mode
file = open("example.txt", "a")
for i in range(1,101):
    file.write(str(i)+"\n")
    
# Read Mode
file = open("example.txt", "r")
# print(file.read())
# reading data line by line
print(file.readline())
print(file.readline())

file.close()
