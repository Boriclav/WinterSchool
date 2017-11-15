A = input()
a = len(A)
q = 0
p = 0
h = 0
if a == 6:
	if A[p] == '1':
		print('сто ', end='')
	if A[p] == '2':
		print('двести ', end='')
	if A[p] == '3':
		print('триста ', end='')
	if A[p] == '4':
		print('четыреста ', end='')
	if A[p] == '5':
		print('пятьсот ', end='')
	if A[p] == '6':
		print('шестьсот ', end='')
	if A[p] == '7':
		print('семьсот ', end='')
	if A[p] == '8':
		print('восемьсот ', end='')
	if A[p] == '9':
		print('девятьсот ', end='')
	a = a - 1
	p = p+1 
if a == 5:
	if A[p] == '1':
		if A[p+1] == '0':
			print('десять ', end='')
		if A[p+1] == '1':
			print('одиннадцать ', end='')
		if A[p+1] == '2':
			print('двенадцать ', end='')
		if A[p+1] == '3':
			print('тринадцать ', end='')
		if A[p+1] == '4':
			print('четырнадцать ', end='')
		if A[p+1] == '5':
			print('пятнадцать ', end='')
		if A[p+1] == '6':
			print('шестнадцать ', end='')
		if A[p+1] == '7':
			print('семнадцать ', end='')
		if A[p+1] == '8':
			print('восемнадцать ', end='')
		if A[p+1] == '9':
			print('девятнадцать ', end='')
		q = 1
	if A[p] == '2':
		print('двадцать ', end='')
	if A[p] == '3':
		print('тридцать ', end='')
	if A[p] == '4':
		print('сорок ', end='')
	if A[p] == '5':
		print('пятьдесят ', end='')
	if A[p] == '6':
		print('шестьдесят ', end='')
	if A[p] == '7':
		print('семьдесят ', end='')
	if A[p] == '8':
		print('восемьдесят ', end='')
	if A[p] == '9':
		print('девяносто ', end='')
	a = a - 1
	p = p + 1
if (q == 0) and (a == 4):
	if A[p] == '1':
		print('одна ', end='')
		h = 1
	if A[p] == '2':
		print('две ', end='')
		h = 2
	if A[p] == '3':
		print('три ', end='')
		h = 2
	if A[p] == '4':
		print('четыре ', end='')
		h = 2
	if A[p] == '5':
		print('пять ', end='')
	if A[p] == '6':
		print('шесть ', end='')
	if A[p] == '7':
		print('семь ', end='')
	if A[p] == '8':
		print('восемь ', end='')
	if A[p] == '9':
		print('девять ', end='')
if a == 4:
	a = a - 1
	p = p + 1
	if h ==  0:
		print('тысяч ', end='')
	if h == 1:
		print('тысяча ', end='')
	if h == 2:
		print('тысячи ', end='')
q = 0
if a == 3:
	if A[p] == '1':
		print('сто ', end='')
	if A[p] == '2':
		print('двести ', end='')
	if A[p] == '3':
		print('триста ', end='')
	if A[p] == '4':
		print('четыреста ', end='')
	if A[p] == '5':
		print('пятьсот ', end='')
	if A[p] == '6':
		print('шестьсот ', end='')
	if A[p] == '7':
		print('семьсот ', end='')
	if A[p] == '8':
		print('восемьсот ', end='')
	if A[p] == '9':
		print('девятьсот ', end='')
	a = a - 1
	p = p+1 
if a == 2:
	if A[p] == '1':
		if A[p+1] == '0':
			print('десять ', end='')
		if A[p+1] == '1':
			print('одиннадцать ', end='')
		if A[p+1] == '2':
			print('двенадцать ', end='')
		if A[p+1] == '3':
			print('тринадцать ', end='')
		if A[p+1] == '4':
			print('четырнадцать ', end='')
		if A[p+1] == '5':
			print('пятнадцать ', end='')
		if A[p+1] == '6':
			print('шестнадцать ', end='')
		if A[p+1] == '7':
			print('семнадцать ', end='')
		if A[p+1] == '8':
			print('восемнадцать ', end='')
		if A[p+1] == '9':
			print('девятнадцать ', end='')
		q = 1
	if A[p] == '2':
		print('двадцать ', end='')
	if A[p] == '3':
		print('тридцать ', end='')
	if A[p] == '4':
		print('сорок ', end='')
	if A[p] == '5':
		print('пятьдесят ', end='')
	if A[p] == '6':
		print('шестьдесят ', end='')
	if A[p] == '7':
		print('семьдесят ', end='')
	if A[p] == '8':
		print('восемьдесят ', end='')
	if A[p] == '9':
		print('девяносто ', end='')
	a = a - 1
	p = p + 1
if (q == 0) and (a == 1):
	if A[p] == '1':
		print('один ', end='')
	if A[p] == '2':
		print('два ', end='')
	if A[p] == '3':
		print('три ', end='')
	if A[p] == '4':
		print('четыре ', end='')
	if A[p] == '5':
		print('пять ', end='')
	if A[p] == '6':
		print('шесть ', end='')
	if A[p] == '7':
		print('семь ', end='')
	if A[p] == '8':
		print('восемь ', end='')
	if A[p] == '9':
		print('девять ', end='')

	
