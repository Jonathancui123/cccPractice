import time

n = int(input())
datainput = input()
data = list(map(int, datainput.split(' ')))
mins = []
maxs = []
reorder = []

start = time.time()

while len(data) > 0:
	mins.append(min(data))
	data.remove(min(data))
	if len(data) > 0:
		maxs.append(max(data))
		data.remove(max(data))

mins.reverse()
maxs.reverse()

zipped = zip(mins, maxs)

for i in zipped:
	for j in i:
		reorder.append(j)

reorder = list(map(str, reorder))

print(' '.join(reorder))
print(time.time() - start)