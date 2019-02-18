s = input()
max = [s[0]]

def check(str):
	temp = list(str)
	for a in range(len(temp)-1):
		if temp[a+1] < temp[a]:
			return False
			break
	return True

# go short to long
for i in range(len(s)): # first char
	for j in range(i, len(s)): # last char
		if check(s[i:j]) and j-i > len(max):
			max = s[i:j]

print('Longest substring in alphabetical order is:')
print(''.join(max))