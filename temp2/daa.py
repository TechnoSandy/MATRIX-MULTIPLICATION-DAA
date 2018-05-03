
size1 = 0
size2 = 0

def isSmall(a,b):
	if len(a) > len(b):
		return False
	elif len(b) > len(a):
		return True
	for i in range(len(a)):
		if int(a[i]) < int(b[i]):
			return True
		elif int(a[i]) > int(b[i]):
			return False 

def diff(a,b):
	if isSmall(a,b):
		temp=b; b=a; a=temp
	a = a[::-1]
	b = b[::-1]
	carry=0
	a = list(a); b=list(b)
	for i in range(len(b)):
		sm = int(a[i])-int(b[i])-carry
		if sm<0:
			sm = sm + 10
			carry=1
		else:
			carry=0
		a[i]=str(sm)		
	for i in range(len(b), len(a)):
		sm = int(a[i])-carry
		if sm<0:
			sm = sm + 10
			carry=1
		else:
			carry=0
		a[i]=str(sm)
	a=''.join(a)
	a=a[::-1]
	return a

def add(a,b):
	a = a[::-1]
	b = b[::-1]
	if len(a)>len(b):
		temp=b; b=a; a=temp
	carry=0
	a = list(a); b=list(b)
	for i in range(len(a)):
		sm = int(a[i])+int(b[i])+carry
		carry=sm/10 ; sm=sm%10 ; b[i]=str(sm)		
	for i in range(len(a), len(b)):
		sm = int(b[i])+carry
		carry=sm/10 ; sm=sm%10 ;b[i]=str(sm)
	if carry:
		b.append(str(carry))
	b=''.join(b)
	b=b[::-1]
	return b

def splitMultiplicants(mul, length):
	return mul[:length], mul[length:]

def makeEqualLen(a,b):
	if len(a)>len(b):
		b='0'*(len(a)-len(b))+b
	elif len(b)>len(a):
		a='0'*(len(b)-len(a))+a
	return a,b

def KaratsubaLargeMultiply(a,b):
	a,b = makeEqualLen(a,b)
	if len(a) == 1:
		return str(int(a)*int(b))
	if len(a)%2:
		m2 = 1+len(a)/2
	else:
		m2 = len(a)/2
	sh = len(a)-m2
	A, B = splitMultiplicants(a,m2)
	C, D = splitMultiplicants(b,m2)

	AC = KaratsubaLargeMultiply(A,C)
	PQ = KaratsubaLargeMultiply(add(A,B),add(C,D))
	BD = KaratsubaLargeMultiply(B,D)

	return (add(add(AC+'0'*(2*sh), diff(PQ,add(AC,BD))+'0'*sh), BD)).lstrip('0')

def split(string):
	data = string.split(',',3)
	return int(data[0].lstrip('('))-1, int(data[1])-1, data[2].rstrip(')')

def conventionalO3(matrix1, matrix2, size1, size2):
	matrix3 =[['0' for x in range(size2)] for y in range(size2)]
	for i in range(size1):
		for j in range(size2):
			for k in range(size1):
				matrix3[i][j] = add(KaratsubaLargeMultiply(matrix1[i][k], matrix2[k][j]), matrix3[i][j])
	return matrix3

def MatrixAdd(A, B):
    n = len(A)
    C = [[0 for j in xrange(0, n)] for i in xrange(0, n)]
    for i in xrange(0, n):
        for j in xrange(0, n):
			if A[i][j][0]=='-' and B[i][j][0]=='-':
				C[i][j] = add(A[i][j][1:],B[i][j][1:])
				C[i][j] = '-'+C[i][j]
			elif (B[i][j][0]=='-' and A[i][j][0] != '-'):
				C[i][j] = diff(A[i][j], B[i][j][1:])
				if isSmall(A[i][j], B[i][j][1:]):
					C[i][j] = '-'+C[i][j]
			elif (B[i][j][0]!='-' and A[i][j][0] == '-'):
				C[i][j] = diff(A[i][j][1:], B[i][j])
				if isSmall(B[i][j],A[i][j][1:]):
					C[i][j] = '-'+C[i][j]											
			else:
				C[i][j] = add(A[i][j],B[i][j])
    return C

def MatrixSubtract(A, B):
    n = len(A)
    C = [[0 for j in xrange(0, n)] for i in xrange(0, n)]
    for i in xrange(0, n):
        for j in xrange(0, n):
			if A[i][j][0]=='-' and B[i][j][0]=='-':
				C[i][j] = diff(A[i][j][1:],B[i][j][1:])
				if isSmall(B[i][j][1:],A[i][j][1:]):
					C[i][j] = '-'+C[i][j]
			elif (B[i][j][0]=='-' and A[i][j][0] != '-'):
				C[i][j] = add(A[i][j], B[i][j][1:])
			elif (B[i][j][0]!='-' and A[i][j][0] == '-'):
				C[i][j] = add(A[i][j][1:], B[i][j])
				C[i][j] = '-'+C[i][j]											
			else:
				C[i][j] = diff(A[i][j],B[i][j])
				if isSmall(A[i][j],B[i][j]):
					C[i][j] = '-'+C[i][j]
    return C

def Strassen(A,B):
	if len(A) == 1:
		print ('A = %d B =%d'%(int(A[0][0]), int(B[0][0])))
		return str(int(A[0][0])*int(B[0][0]))
	orgSize = len(A)
	size = len(A)/2
	a = [[0 for i in range(size)] for j in range(size)]
	b = [[0 for i in range(size)] for j in range(size)]
	c = [[0 for i in range(size)] for j in range(size)]
	d = [[0 for i in range(size)] for j in range(size)]
	e = [[0 for i in range(size)] for j in range(size)]
	f = [[0 for i in range(size)] for j in range(size)]
	g = [[0 for i in range(size)] for j in range(size)]
	h = [[0 for i in range(size)] for j in range(size)]
	
	for i in range(size):
		for j in range(size):
			a[i][j] = A[i][j]
			b[i][j] = A[i][size+j]
			c[i][j] = A[size+i][j]
			d[i][j] = A[size+i][size+j]
			e[i][j] = B[i][j]
			f[i][j] = B[i][size+j]
			g[i][j] = B[size+i][j]
			h[i][j] = A[size+i][size+j]
	p1 = Strassen(a,MatrixSubtract(f,h))
	p2 = Strassen(MatrixAdd(a,b),h)
	p3 = Strassen(MatrixAdd(c,d),e)	
	p4 = Strassen(MatrixSubtract(g,e),d)
	p5 = Strassen(MatrixAdd(a,d),MatrixAdd(e,h))
	p6 = Strassen(MatrixSubtract(b,d),MatrixAdd(g,h))
	p7 = Strassen(MatrixSubtract(a,c),MatrixAdd(e,f))
	print p1,p2,p3,p4,p5,p6,p7
	
	c01 = MatrixAdd(p1,p2)
	c10 = MatrixAdd(p3,p4)
	c00 = MatrixSubtract(MatrixAdd()
	c11 = 
	C = [['0' for i in range(orgSize)] for j in range(orgSize)]
	for i in range(size):
		for j in range(size):
			C[i][j] = 
			C[i][j+size] = 
			C[i+size][j] = 
			C[i+size][j+size] = 
	return C

def StrassenMultiply(matrix1, matrix2, matrix3):
	a = matrix1[0][0]; b = matrix1[0][1] ; c = matrix1[1][0] ; d = matrix1[1][1]
	e = matrix2[0][0]; f = matrix2[0][1] ; g = matrix2[1][0] ; h = matrix2[1][1]
	p1 = KaratsubaLargeMultiply(a,diff(f,h))
	p2 = KaratsubaLargeMultiply(add(a,b),h)
	p3 = KaratsubaLargeMultiply(add(c,d),e)	
	p4 = KaratsubaLargeMultiply(diff(g,e),d)
	p5 = KaratsubaLargeMultiply(add(a,d),add(e,h))
	p6 = KaratsubaLargeMultiply(diff(b,d),add(g,h))
	p7 = KaratsubaLargeMultiply(diff(a,c),add(e,f))
	p1N = 0; p4N = 0; p6N = 0; p7N=0
	
	if isSmall(f,h):
		p1N = 1
		matrix3[0][1] = diff(p2,p1).lstrip('0')
		if isSmall(p2,p1):
			matrix3[0][1] = '-'+matrix3[0][1]
	else:
		matrix3[0][1] = add(p1,p2).lstrip('0')

	if isSmall(g,e):
		p4N = 1
		matrix3[1][0] = diff(p3,p4).lstrip('0')
		if isSmall(p3,p4):
			matrix3[1][0] = '-'+matrix3[1][0]
	else:
		matrix3[1][0] = add(p3,p4).lstrip('0')

	if isSmall(b,d):
		p6N = 1
	if isSmall(a,c):
		p7N = 1

	if (p1N == 0 and p7N==0):
		A = add(p1,p5)
		B = add(p3,p7)
		matrix3[1][1] = diff(A,B).lstrip('0')
		if isSmall(A,B):
			matrix3[1][1] = '-'+matrix3[1][1]
	elif (p1N == 0 and p7N==1):
		A = add(add(p1,p5),p7)
		matrix3[1][1] = diff(A,p3).lstrip('0')
		if isSmall(A,p3):
			matrix3[1][1] = '-'+matrix3[1][1]
	elif (p1N == 1 and p7N==0):
		A = add(p5,add(p3,p7))
		matrix3[1][1] = diff(p1,A).lstrip('0')
		if isSmall(p1,A):
			matrix3[1][1] = '-'+matrix3[1][1]
	elif (p1N == 1 and p7N==1):
		A = add(p1,add(p3,p7))
		matrix3[1][1] = diff(p5,A).lstrip('0')
		if isSmall(p5,A):
			matrix3[1][1] = '-'+matrix3[1][1]

	if (p4N == 0 and p6N == 0):
		A = add(add(p5,p4),p6)
		matrix3[0][0] = diff(A,p2).lstrip('0')
		if isSmall(A,p2):
			matrix3[0][0] = '-'+matrix3[0][0]			
	elif(p4N == 0 and p6N == 1):
		A = add(p5,p4)
		B = add(p6,p2)
		matrix3[0][0] = diff(A,B).lstrip('0')
		if isSmall(A,B):
			matrix3[0][0] = '-'+matrix3[0][0]
	elif(p4N == 1 and p6N == 0):
		A = add(p5,p6)
		B = add(p4,p2)
		matrix3[0][0] = diff(A,B).lstrip('0')
		if isSmall(A,B):
			matrix3[0][0] = '-'+matrix3[0][0]
	elif(p4N == 1 and p6N == 1):
		A = add(add(p6,p4),p2)
		matrix3[0][0] = diff(p5,A).lstrip('0')
		if isSmall(p5,A):
			matrix3[0][0] = '-'+matrix3[0][0]

	return matrix3
class matrixElement:
	def __init__(self, row,col):
		self.row = row
		self.col = col
		self.value = '0'
		self.sign = '+'


f = open('out.txt', 'r') 
w = open('2out.txt', 'r')
i = f.readline()
j = w.readline()

size1 = int(i.rstrip())
matrix1 =[['0' for x in range(size1)] for y in range(size1)]
for i in f:			
	a,b,c = split(i.rstrip())
	matrix1[a][b] = c

size2 = int(j.rstrip())
matrix2 =[['0' for x in range(size2)] for y in range(size2)]
for j in w:
	a,b,c = split(j.rstrip())
	matrix2[a][b] = c

matrix3 =[['0' for x in range(size2)] for y in range(size2)]

Strassen(matrix1, matrix2)
