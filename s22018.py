from math import ceil

n = int(input())
data = []
swaps = (n-2)*2

for i in range(n):
	data.append(
		list(map(int, input().split(' ')))
		)

print(data)

'''
def swap(a, b, c, d):
	temp = a
	a = d
	d = c
	c = b
	b = temp
	return None
'''
def swap4(data, row, col, n):
	temp = data[row][col]
	data[row][col] = data[n-col-1][row]
	data[n-col-1][row] = data[n-row-1][n-col-1]
	data[n-row-1][n-col-1] = data[col][n-row-1]
	data[col][n-row-1] = temp
	# swap(data[row][col], data[col][n-row-1], data[n-row-1][n-col-1], data[n-col-1][row])
	return None

def rotate(data, n):
	for i in range(ceil(n/2)):
		for j in range(i,n-i-1):
			swap4(data, i, j, n)
	return None

def check(data):
	for i in range(n):
		for j in range(n-1):
			if data[i][j+1] <= data[i][j]:
				return False
	for i in range(n-1):
		if data[i][0] > data[i+1][0]:
			return False
	return True

while check(data) == False:
# for i in range(4):
	rotate(data, n)


for j in range(n):
	print(' '.join(list(map(str, data[j]))))