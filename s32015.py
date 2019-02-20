g = int(input()) # gates
p = int(input()) # planes
gates = [None for i in range(g)]
requests = []
landed = 0

for i in range(p):
	requests.append(int(input()))

for request in requests:
	for i in range(request-1, -1, -1):
		if not gates[i]:
			gates[i] = 1
			landed += 1
			break
		else:
			available = [gates.index(x) for x in gates if x == None and gates.index(x) <= request-1]
			if available:
				nextavail = max(available)
			else:
				nextavail = None
			if nextavail:
				gates[nextavail] = 1
				landed += 1
				break
			else:
				break
				break

print(landed)