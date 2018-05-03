def add(a,b):
# Reverse the Strings
	a = a[::-1]
	b = b[::-1]
# Place string of smaller length in b
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

# Place string of smaller length in b
	if isSmall(a,b):
		temp=b; b=a; a=temp
# Reverse the Strings
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

def multiply(a,b):
	product = [0]*(len(a)+len(b));
	i_n1=0
	i_n2=0
	for i in xrange(len(a)-1,-1,-1):
		carry=0
		i_n2=0	
		for j in xrange(len(b)-1,-1,-1):
			sm = carry+product[i_n1+i_n2]+(int(a[i])*int(b[j]))
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

def splitMultiplicants(mul, length):
	return mul[:length], mul[length:]

def makeEqualLen(a,b):
	if len(a)>len(b):
		b='0'*(len(a)-len(b))+b
	elif len(b)>len(a):
		a='0'*(len(b)-len(a))+a
	return a,b

def GausslargeMultiply(a,b):
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
	
	AC = GausslargeMultiply(A,C)
	AD = GausslargeMultiply(A,D)
	BC = GausslargeMultiply(B,C)
	BD = GausslargeMultiply(B,D)
	return add(add(AC+'0'*(2*sh),add(AD,BC)+'0'*sh), BD)
	 
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

	return add(add(AC+'0'*(2*sh), diff(PQ,add(AC,BD))+'0'*sh), BD)


print GausslargeMultiply('75812870870640031822622711122388','34392492118618028435332620947927')
print KaratsubaLargeMultiply('75812870870640031822622711122388','34392492118618028435332620947927')
print multiply('75812870870640031822622711122388','34392492118618028435332620947927')

