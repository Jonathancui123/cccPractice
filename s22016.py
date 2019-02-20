choice = int(input())
n = int(input())
dmoj = sorted(list(map(int, input().split(' '))))
peg = sorted(list(map(int, input().split(' '))))
speed = 0

if choice == 1:
	for i in range(n):
		speed += max(dmoj[i], peg[i])
elif choice == 2:
	peg.reverse()
	for i in range(n):
		speed += max(dmoj[i], peg[i])

print(speed)