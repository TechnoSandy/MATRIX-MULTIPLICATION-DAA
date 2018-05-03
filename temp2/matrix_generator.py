'''
matrix_generator.py

Property of :
	1. Priyank Arora
	2. Sandeep Satome
	3. Harshini 
	4. Kelvin Thomas

'''
import random
import sys as sys
import os as os

def generate(number):
    return int("1"+"0"*(number-1)),int("9"*number)

def main(argv):
	if len(argv) < 4:
		print('Command Usage:\n $> python number_generator.py <NUM> <filename.txt> <SizeOfArray>')
		sys.exit(0)
	elif int(argv[1]) < 0 or int(argv[3]) < 0:
		print('range of the all number should be positive')
		sys.exit(0)
	a, column = generate(pow(2,int(argv[1])))
	with open(argv[2], 'w') as f, open('2'+argv[2], 'w') as l:
		f.write('%d \n'%(int (argv[3])))
		l.write('%d \n'%(int (argv[3])))
		for i in range(1,int(argv[3])+1):
			for j in range(1,int(argv[3])+1):
				f.write('(%d,%d,%d) \n'%(i,j,random.randint(a,column)))
				l.write('(%d,%d,%d) \n'%(i,j,random.randint(a,column)))

'''
	os.system('cat %s'%(argv[2]))
	print("\n")
	os.system('cat %s'%('2'+argv[2]))
'''

if __name__ == "__main__":
	main(sys.argv)

