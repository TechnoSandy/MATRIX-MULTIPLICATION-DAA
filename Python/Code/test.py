var1 = '999922'
var =  '55'
add = [0]*(max(len(var),len(var1))+1)
l=len(add)-1
carry=0
for i,j in zip(range(len(var)-1,-1,-1),range(len(var1)-1,-1,-1)):
	print i,j



'''
	add[l]= carry+int(var[i])+int(var1[j])
	carry = add[l]/10
	add[l] %= 10
	l = l-1
add[0] = carry
print ''.join(str(x) for x in add)
'''


