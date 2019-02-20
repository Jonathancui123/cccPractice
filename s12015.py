k = int(input())
numbers = []

for i in range(k):
	entry = int(input())
	if entry != 0:
		numbers.append(entry)
	else:
		numbers.pop()

print(sum(numbers))