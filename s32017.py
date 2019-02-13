n = int(input())
lengths = list(map(int, input().split(' ')))
sums = []

lengths.sort()

for i in range(n - 1):
	for j in range(i + 1, n):
		if lengths[i] + lengths[j] not in [asum[0] for asum in sums]:
			sums.append([lengths[i] + lengths[j], 1])
		else:
			for a, b in enumerate([asum[0] for asum in sums]):
				if b == lengths[i] + lengths[j]:
					sums[a][1] += 1

maxlength = max([asum[1] for asum in sums])
ways = len([asum[1] for asum in sums if asum[1] == maxlength])

print(str(maxlength) + ' ' + str(ways))