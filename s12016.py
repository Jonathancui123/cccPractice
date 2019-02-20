str1 = sorted(list(input()))
str2 = sorted(list(input()))
check = True
limit = len(str1)

print(str1, str2)

while True:
	if not str1:
		print('A')
		break
	elif str1[0] in str2:
		temp = str1[0]
		str1.remove(temp)
		str2.remove(temp)
	elif '*' in str2:
		del str1[0]
		str2.remove('*')
	else:
		print('N')
		break