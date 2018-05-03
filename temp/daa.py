


import random
import matplotlib.pyplot as plt
import os as os
import sys as sys

size1 = 0
size2 = 0


def isSmall(row, column):
	if len(row) > len(column):
		return False
	elif len(column) > len(row):
		return True
	for i in range(len(row)):
		if int(row[i]) < int(column[i]):
			return True
		elif int(row[i]) > int(column[i]):
			return False 


def diff(row, column):
	if isSmall(row, column):
		temp = column; column = row; row = temp
	row = row[::-1]
	column = column[::-1]
	carry = 0
	row = list(row); column = list(column)
	for i in range(len(column)):
		sm = int(row[i]) - int(column[i]) - carry
		if sm < 0:
			sm = sm + 10
			carry = 1
		else:
			carry = 0
		row[i] = str(sm)		
	for i in range(len(column), len(row)):
		sm = int(row[i]) - carry
		if sm < 0:
			sm = sm + 10
			carry = 1
		else:
			carry = 0
		row[i] = str(sm)
	row = ''.join(row)
	row = row[::-1]
	return row


def add(row, column):
	row = row[::-1]
	column = column[::-1]
	if len(row) > len(column):
		temp = column; column = row; row = temp
	carry = 0
	row = list(row); column = list(column)
	for i in range(len(row)):
		sm = int(row[i]) + int(column[i]) + carry
		carry = sm / 10 ; sm = sm % 10 ; column[i] = str(sm)		
	for i in range(len(row), len(column)):
		sm = int(column[i]) + carry
		carry = sm / 10 ; sm = sm % 10 ;column[i] = str(sm)
	if carry:
		column.append(str(carry))
	column = ''.join(column)
	column = column[::-1]
	return column


def splitMultiplicants(mul, length):
	return mul[:length], mul[length:]


def makeEqualLen(row, column):
	if len(row) > len(column):
		column = '0' * (len(row) - len(column)) + column
	elif len(column) > len(row):
		row = '0' * (len(column) - len(row)) + row
	return row, column


def KaratsubaLargeMultiply(row, column):
	row, column = makeEqualLen(row, column)
	if len(row) == 1:
		return str(int(row) * int(column))
	if len(row) % 2:
		m2 = 1 + len(row) / 2
	else:
		m2 = len(row) / 2
	sh = len(row) - m2
	A, B = splitMultiplicants(row, m2)
	C, D = splitMultiplicants(column, m2)

	AC = KaratsubaLargeMultiply(A, C)
	PQ = KaratsubaLargeMultiply(add(A, B), add(C, D))
	BD = KaratsubaLargeMultiply(B, D)

	return (add(add(AC + '0' * (2 * sh), diff(PQ, add(AC, BD)) + '0' * sh), BD)).lstrip('0')


def split(string):
	data = string.split(',', 3)
	return int(data[0].lstrip('(')) - 1, int(data[1]) - 1, data[2].rstrip(')')


def conventionalMatrixMultiplication(matrix1, matrix2, size1, size2):
	matrix3 = [['0' for x in range(size2)] for y in range(size2)]
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
			if A[i][j][0] == '-' and B[i][j][0] == '-':
				C[i][j] = add(A[i][j][1:], B[i][j][1:])
				C[i][j] = '-' + C[i][j]
			elif (B[i][j][0] == '-' and A[i][j][0] != '-'):
				C[i][j] = diff(A[i][j], B[i][j][1:])
				if isSmall(A[i][j], B[i][j][1:]):
					C[i][j] = '-' + C[i][j]
			elif (B[i][j][0] != '-' and A[i][j][0] == '-'):
				C[i][j] = diff(A[i][j][1:], B[i][j])
				if isSmall(B[i][j], A[i][j][1:]):
					C[i][j] = '-' + C[i][j]											
			else:
				C[i][j] = add(A[i][j], B[i][j])
			return C


def MatrixSubtract(A, B):
	n = len(A)
	C = [[0 for j in xrange(0, n)] for i in xrange(0, n)]
	for i in xrange(0, n):
		for j in xrange(0, n):
			if str(A[i][j][0]) == '-' and str(B[i][j][0]) == '-':
				C[i][j] = diff(A[i][j][1:], B[i][j][1:])
				if isSmall(B[i][j][1:], A[i][j][1:]):
					C[i][j] = '-' + C[i][j]
			elif (B[i][j][0] == '-' and A[i][j][0] != '-'):
				C[i][j] = add(A[i][j], B[i][j][1:])
			elif (B[i][j][0] != '-' and A[i][j][0] == '-'):
				C[i][j] = add(A[i][j][1:], B[i][j])
				C[i][j] = '-' + C[i][j]											
			else:
				C[i][j] = diff(A[i][j], B[i][j])
				if isSmall(A[i][j], B[i][j]):
					C[i][j] = '-' + C[i][j]
			return C


def Strassen(A, B):
	if len(A) == 1:
		return str(int(A[0][0]) * int(B[0][0]))
	orgSize = len(A)
	size = len(A) / 2
	row = [[0 for i in range(size)] for j in range(size)]
	column = [[0 for i in range(size)] for j in range(size)]
	value = [[0 for i in range(size)] for j in range(size)]
	d = [[0 for i in range(size)] for j in range(size)]
	e = [[0 for i in range(size)] for j in range(size)]
	f = [[0 for i in range(size)] for j in range(size)]
	g = [[0 for i in range(size)] for j in range(size)]
	h = [[0 for i in range(size)] for j in range(size)]
	 
	for i in range(size):
		for j in range(size):
			row[i][j] = A[i][j]
			column[i][j] = A[i][size + j]
			value[i][j] = A[size + i][j]
			d[i][j] = A[size + i][size + j]
			e[i][j] = B[i][j]
			f[i][j] = B[i][size + j]
			g[i][j] = B[size + i][j]
			h[i][j] = A[size + i][size + j]
	p1 = Strassen(row, MatrixSubtract(f, h))
	p2 = Strassen(MatrixAdd(row, column), h)
	p3 = Strassen(MatrixAdd(value, d), e)	
	p4 = Strassen(MatrixSubtract(g, e), d)
	p5 = Strassen(MatrixAdd(row, d), MatrixAdd(e, h))
	p6 = Strassen(MatrixSubtract(column, d), MatrixAdd(g, h))
	p7 = Strassen(MatrixSubtract(row, value), MatrixAdd(e, f))
	print(list(p1))
	print("ALL P VALUES")
	print p1, p2, p3, p4, p5, p6, p7
	
	#===========================================================================
	# c11 = p5+p4-p2+p6
	# c12 = p1+p2
	# c21 = p3+p4
	# c22 = p1+p5-p3-p7
	#===========================================================================
	# c11 = p5+p4-p2+p6
	c11 = MatrixAdd(MatrixSubtract(MatrixAdd(p5, p4), p2), p6)

	# c12 = p1+p2
	c12 = MatrixAdd(p1, p2)

	# c21 = p3 + p4
	c21 = MatrixAdd(p3, p4)

	# c22 = p1 + p3 - p2 + p6
	c22 = MatrixAdd(MatrixSubtract(MatrixAdd(p1, p3), p2), p6)
	
	C = [['0' for i in range(orgSize)] for j in range(orgSize)]
	for i in range(size):
		for j in range(size):
			C[i][j] = c11[i][j]
			C[i][j + size] = c12[i][j]
			C[i + size][j] = c21[i][j]
			C[i + size][j + size] = c22[i][j]
	return C


def StrassenMultiply(matrix1, matrix2, matrix3):
	row = matrix1[0][0]
	column = matrix1[0][1]
	value = matrix1[1][0]
	d = matrix1[1][1]
	e = matrix2[0][0]
	f = matrix2[0][1] 
	g = matrix2[1][0]
	h = matrix2[1][1]
	p1 = KaratsubaLargeMultiply(row, diff(f, h))
	p2 = KaratsubaLargeMultiply(add(row, column), h)
	p3 = KaratsubaLargeMultiply(add(value, d), e)	
	p4 = KaratsubaLargeMultiply(diff(g, e), d)
	p5 = KaratsubaLargeMultiply(add(row, d), add(e, h))
	p6 = KaratsubaLargeMultiply(diff(column, d), add(g, h))
	p7 = KaratsubaLargeMultiply(diff(row, value), add(e, f))
	p1N = 0; p4N = 0; p6N = 0; p7N = 0
	
	if isSmall(f, h):
		p1N = 1
		matrix3[0][1] = diff(p2, p1).lstrip('0')
		if isSmall(p2, p1):
			matrix3[0][1] = '-' + matrix3[0][1]
	else:
		matrix3[0][1] = add(p1, p2).lstrip('0')

	if isSmall(g, e):
		p4N = 1
		matrix3[1][0] = diff(p3, p4).lstrip('0')
		if isSmall(p3, p4):
			matrix3[1][0] = '-' + matrix3[1][0]
	else:
		matrix3[1][0] = add(p3, p4).lstrip('0')

	if isSmall(column, d):
		p6N = 1
	if isSmall(row, value):
		p7N = 1

	if (p1N == 0 and p7N == 0):
		A = add(p1, p5)
		B = add(p3, p7)
		matrix3[1][1] = diff(A, B).lstrip('0')
		if isSmall(A, B):
			matrix3[1][1] = '-' + matrix3[1][1]
	elif (p1N == 0 and p7N == 1):
		A = add(add(p1, p5), p7)
		matrix3[1][1] = diff(A, p3).lstrip('0')
		if isSmall(A, p3):
			matrix3[1][1] = '-' + matrix3[1][1]
	elif (p1N == 1 and p7N == 0):
		A = add(p5, add(p3, p7))
		matrix3[1][1] = diff(p1, A).lstrip('0')
		if isSmall(p1, A):
			matrix3[1][1] = '-' + matrix3[1][1]
	elif (p1N == 1 and p7N == 1):
		A = add(p1, add(p3, p7))
		matrix3[1][1] = diff(p5, A).lstrip('0')
		if isSmall(p5, A):
			matrix3[1][1] = '-' + matrix3[1][1]

	if (p4N == 0 and p6N == 0):
		A = add(add(p5, p4), p6)
		matrix3[0][0] = diff(A, p2).lstrip('0')
		if isSmall(A, p2):
			matrix3[0][0] = '-' + matrix3[0][0]			
	elif(p4N == 0 and p6N == 1):
		A = add(p5, p4)
		B = add(p6, p2)
		matrix3[0][0] = diff(A, B).lstrip('0')
		if isSmall(A, B):
			matrix3[0][0] = '-' + matrix3[0][0]
	elif(p4N == 1 and p6N == 0):
		A = add(p5, p6)
		B = add(p4, p2)
		matrix3[0][0] = diff(A, B).lstrip('0')
		if isSmall(A, B):
			matrix3[0][0] = '-' + matrix3[0][0]
	elif(p4N == 1 and p6N == 1):
		A = add(add(p6, p4), p2)
		matrix3[0][0] = diff(p5, A).lstrip('0')
		if isSmall(p5, A):
			matrix3[0][0] = '-' + matrix3[0][0]

	return matrix3


class matrixElement:

	def __init__(self, row, col):
		self.row = row
		self.col = col
		self.value = '0'
		self.sign = '+'


# Code Generator
def generate(number):
	return int("1" + "0"*(number - 1)), int("9"*number)


def multiply(row,column):
	product = [0]*(len(row)+len(column));
	i_n1=0
	i_n2=0
	for i in xrange(len(row)-1,-1,-1):
		carry=0
		i_n2=0	
		for j in xrange(len(column)-1,-1,-1):
			sm = carry+product[i_n1+i_n2]+(int(row[i])*int(column[j]))
			carry = sm/10
			product[i_n1+i_n2]= sm%10
			i_n2+=1
		if carry:
			product[i_n1+i_n2] += carry
		i_n1+=1
	#check if all number are zeros
	if product.count('0') == len(product):
		return '0'
		
	strTrev = ''.join(str(x) for x in product)
	strTrev = strTrev[::-1]
	return strTrev.lstrip('0')



def GausslargeMultiply(row,column):
	row,column = makeEqualLen(row,column)
	if len(row) == 1:
		return str(int(row)*int(column))
	if len(row)%2:
		m2 = 1+len(row)/2
	else:
		m2 = len(row)/2
	sh = len(row)-m2
	A, B = splitMultiplicants(row,m2)
	C, D = splitMultiplicants(column,m2)
	
	AC = GausslargeMultiply(A,C)
	AD = GausslargeMultiply(A,D)
	BC = GausslargeMultiply(B,C)
	BD = GausslargeMultiply(B,D)
	return add(add(AC+'0'*(2*sh),add(AD,BC)+'0'*sh), BD)


def main(argv):
	if len(argv) < 4:
		print('Command Usage:\n $> python daa.py <NUM> <filename.txt> <SizeOfArray>')
		sys.exit(0)
	elif int(argv[1]) < 0 or int(argv[3]) < 0:
		print('range of the all number should be positive')
		sys.exit(0)
	a, b = generate(pow(2, int(argv[1])))
	with open(argv[2], 'w') as f, open('2' + argv[2], 'w') as l:
		f.write('%d \n' % (int (argv[3])))
		l.write('%d \n' % (int (argv[3])))
		for i in range(1, int(argv[3]) + 1):
			for j in range(1, int(argv[3]) + 1):
				f.write('(%d,%d,%d) \n' % (i, j, random.randint(a, b)))
				l.write('(%d,%d,%d) \n' % (i, j, random.randint(a, b)))
	
	
	f = open('demo.txt', 'r') 

	w = open('2demo.txt', 'r')
	i = f.readline()
	j = w.readline()
	
	# Matrix 1
	size1 = int(i.rstrip())
	matrix1 = [['0' for x in range(size1)] for y in range(size1)]
	for i in f:			
		a, b, value = split(i.rstrip())
		matrix1[a][b] = value
	print("Printing Matrix one")
	print(matrix1)
	# Matrix Two
	size2 = int(j.rstrip())
	matrix2 = [['0' for x in range(size2)] for y in range(size2)]
	for j in w:
		a, b, value = split(j.rstrip())
		matrix2[a][b] = value
	print("Printing Matrix two")
	print(matrix2)
	
	matrix3 = [['0' for x in range(size2)] for y in range(size2)]
	
	# print(matrix1, matrix2)
# 	MULTIPLICATION
# 	USE THIS FOR NUMBER GENERATION
# 	a, b = generate(pow(2,int(argv[3])))
	
# 	plotGraph()
	a, b = generate(pow(2,2))
	print("Number one =",a)
	print("Number two =",b)
	print("Printing GausslargeMultiply")
	print GausslargeMultiply(str(a),str(b))
	print("Printing KaratsubaLargeMultiply")
	print KaratsubaLargeMultiply(str(a),str(b))
	print("Printing Conventional multiply")
	print multiply(str(a),str(b))
# 	MATRIX MULTIPLICATION
	print("Conventional Matrix Multiplication")
	print(conventionalMatrixMultiplication(matrix1, matrix2, size1, size2))
# 	print("Printing Strassen Multiply")
# 	print(StrassenMultiply(matrix1, matrix2, matrix3))
# 	print("Printing Strassen")
# 	print(Strassen(matrix1, matrix2))

def plotGraph():
	plt.plot([1,2,3,4])
	plt.ylabel('some numbers')
	plt.show()	

	
if __name__ == "__main__":
	main(sys.argv)
	
