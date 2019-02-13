num = int(input())
FirstLine = input()
LastLine = input()

#Make each line into a list of separate names
a = FirstLine.split()
b = LastLine.split()

first = {}
second = {}

#Make a dictionary with keys from the first line and values from the second line
for count in range(num):
    first[a[count]] = b[count]
    second[b[count]] = a[count]

correct = 0

for element in first:
    if second[element] == first [element] and element != first[element]:
        correct += 1

if correct == num:
    print("good")
else:
    print("bad")

#Make a dictionary with the opposite keys and values
#For loop to check if [element] = x is true in both dictionaries