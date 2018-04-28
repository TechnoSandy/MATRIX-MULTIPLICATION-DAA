import sys as sys

def multiply(a,b):
	product = [0]*(len(a)+len(b))
	for j in xrange(len(b)-1,-1,-1):
		carry=0
		for i in xrange(len(a)-1,-1,-1):
			product[i+j+1] += carry+(int(a[i])*int(b[j]))
			carry = (product[i+j+1])/10
			product[i+j+1] %= 10
		product[j] += carry
	return ''.join(str(x) for x in product)

def SumOfListElement(list1):
	s = list1[0]
	for x in list1[1:]:
		add = [0]*(max(len(s),len(x))+1)
		l=len(add)-1
		carry=0
		for i,j in zip(range(len(s)-1,-1,-1),range(len(x)-1,-1,-1)):
			add[l]= carry+int(s[i])+int(x[j])
			carry = add[l]/10
			add[l] %= 10
			l = l-1
		add[0] = carry
		s= ''.join(str(x) for x in add)
	return s


def splitMultiplicants(mul, length):
	return mul[:length], mul[length:]

def largeMultiply(a,b):
	if len(a) == 1 or len(b) == 1:
		return int(multiply(a,b))		 

	m2 = (max(len(a),len(b))/2)

	A, B = splitMultiplicants(a,m2)
	C, D = splitMultiplicants(b,m2)
	
	AC = largeMultiply(A,C)
	PQ = largeMultiply(SumOfList(A,B), SumOfList(C,D))
	BD = largeMultiply(B,D)

	return (AC*pow(10,2*m2)) + (PQ-BD-AC)*pow(10,m2) + BD

def conventionalMatrixO3(t,k):
	szMtx = int(t[0])
	t = t[1:]
	k = k[1:]
	matrix1 =[[0 for x in range(szMtx)] for y in range(szMtx)] 
	matrix2 =[[0 for x in range(szMtx)] for y in range(szMtx)] 
	matrix3 =[[0 for x in range(szMtx)] for y in range(szMtx)] 
	for i in range(len(t)):
		matrix1[int(t[i][0])-1][int(t[i][1])-1] = list(t[i][2:])
		matrix2[int(k[i][0])-1][int(k[i][1])-1] = list(k[i][2:])

	for i in range(szMtx):
		for j in range(szMtx):
			dummyList=[]
			for k in range(szMtx):
				dummyList.append((multiply(matrix1[i][k], matrix2[k][j])))
			matrix3[i][j]=SumOfListElement(dummyList)
	return matrix3

def strauss(t,k):
	szMtx = int(t[0])
	t = t[1:]
	k = k[1:]
	matrix1 =[[0 for x in range(szMtx)] for y in range(szMtx)] 
	matrix2 =[[0 for x in range(szMtx)] for y in range(szMtx)] 
	matrix3 =[[0 for x in range(szMtx)] for y in range(szMtx)] 
	for i in range(len(t)):
		matrix1[int(t[i][0])-1][int(t[i][1])-1] = list(t[i][2:])
		matrix2[int(k[i][0])-1][int(k[i][1])-1] = list(k[i][2:])
	


		
def main(argv):
	t = []
	k = []
	with open(argv[1],'r') as f, open('2'+argv[1],'r') as w:
		for line in f:
			t.append("".join(c for c in line if c not in '(,) \n'))
		for line in w:
			k.append("".join(c for c in line if c not in '(,) \n'))
	print conventionalMatrixO3(t,k)
	
if __name__=="__main__":
	main(sys.argv)
