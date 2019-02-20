from operator import itemgetter

j = int(input()) # number of jerseys
a = int(input()) # number of athletes
jerseys = []
requests = []
satisfied = 0

def con(size):
	if size == 'S':
		return 1
	elif size == 'M':
		return 2
	elif size == 'L':
		return 3

for i in range(j):
	size = con(input())
	jerseys.append((size, i + 1))
for i in range(a):
	request = input().split(' ')
	request[0] = con(request[0])
	request[1] = int(request[1])
	requests.append(request)

print(jerseys)
print(requests)

for jersey in jerseys:
	requests2 = [request for request in requests if request[1] == jersey[1]]
	for request in requests2:
		if jersey[0] >= request[0]:
			satisfied += 1
			break


print(satisfied)