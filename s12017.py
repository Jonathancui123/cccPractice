n = int(input())
sw = list(map(int, input().split(' ')))
se = list(map(int, input().split(' ')))
swsum = 0
sesum = 0
maxi = 0

for i in range(n):
	swsum += sw[i]
	sesum += se[i]
	if swsum == sesum:
		maxi = i + 1

print(maxi)