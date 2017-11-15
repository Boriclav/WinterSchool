n = 10
m = 10
q = 1
A = [[0,0,0,0,0,0,0,0,0,0],
	[0,0,0,0,0,0,0,0,0,0],
	[0,0,0,0,0,0,0,0,0,0],
	[0,0,0,0,0,0,0,0,0,0],
	[0,0,0,0,0,0,0,0,0,0],
	[0,0,0,0,0,0,0,0,0,0],
	[0,0,0,0,0,0,0,0,0,0],
	[0,0,0,0,0,0,0,0,0,0],
	[0,0,0,0,0,0,0,0,0,0],
	[0,0,0,0,0,0,0,0,0,0],
	[0,0,0,0,0,0,0,0,0,0]]
x = int(input('input x-coordinate'))
y = int(input('input y-coordinate'))
while q == 1:
	R = input()
	a = x
	b = y
	if R == 'w':
		y =  y + 1
	elif R == 's':
		y =  y - 1
	elif R == 'a':
		x =  x + 1
	elif R == 'd':
		x =  x - 1
	elif R == 'e':
		break
	A[y][x] = 1
	A[b][a] = 0
	for i in range (n):
		for j in range (n):
			if A[i][j] == 0:
				print('0', end='')
			else:
				print('x', end='')
		print('\n', end= '')
	
	

	
