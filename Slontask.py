
import sys,tty,termios, os
class _Getch:
	def __call__(self):
			fd = sys.stdin.fileno()
			old_settings = termios.tcgetattr(fd)
			try:
				tty.setraw(sys.stdin.fileno())
				ch = sys.stdin.read(3)
			finally:
				termios.tcsetattr(fd, termios.TCSADRAIN, old_settings)
			return ch
def get():
        inkey = _Getch()
        while(1):
                k=inkey()
                if k!='':break
        if k=='\x1b[A':
                print ("up")
                return ('w')
        elif k=='\x1b[B':
                print ("down")
                return('s')
        elif k=='\x1b[C':
                print ("right")
                return('d')
        elif k=='\x1b[D':
                print ("left")
                return('a')
        else:
                print ("not an arrow key!")
                return('e')
n = 10
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
if (x > 9) or (y > 9)  or (x < 0) or (y < 0):
	print('Error')
else:
	A[y][x] = 1
	os.system('clear')
	for i in range (n):
		for j in range (n):
			if A[i][j] == 0:
				print('0', end='')
			else:
				print('x', end='')
		print('\n', end= '')
	while q == 1:
		print('put buttom for movement')
		R = get()
		a = x
		b = y
		if R == 'w':
			y =  y - 1
		elif R == 's':
			y =  y + 1
		elif R == 'a':
			x =  x - 1
		elif R == 'd':
			x =  x + 1
		elif R == 'e':
			break
		if (x > 9) or (y > 9)  or (x < 0) or (y < 0):
			print('Error')
			x = a
			y = b
		else:	
			A[y][x] = 1
			A[b][a] = 0
			os.system('clear')
			for i in range (n):
				for j in range (n):
					if A[i][j] == 0:
						print('0', end='')
					else:
						print('x', end='')
				print('\n', end= '')
	
	

	
