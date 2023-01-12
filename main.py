# control structures
flag = True
i = 1

if flag:
    print("our if is true")
else:
    print("our if is false")

while i < 10:
    print("In loop", i)
    i *= 2

for j in range (1, 15, 1):
    print("for loop: ", j)

# keyboard io
kInput = input("Please enter a number: ")
print("Your number is:", kInput)

num = int(kInput) + 10

print("Added ten to your number:", num)

# file io
with open("input.txt", "r") as file:
    for line in file:
        values = line.split()
        print(values)

ofile = open("output.txt", "w")

ofile.write("abcdefg\nhijklmn\n")