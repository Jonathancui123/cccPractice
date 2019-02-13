n = int(input())
positions = []
borders = []
sizes = []

for i in range(n):
	positions.append(int(input()))

positions.sort()

for i in range(n-1):
	borders.append(
		(positions[i + 1] + positions[i])/2
		)

for i in range(n-2):
	sizes.append(
		borders[i+1] - borders[i]
		)

print(min(sizes))