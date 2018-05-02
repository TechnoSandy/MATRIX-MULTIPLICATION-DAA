import sys as sys


def multiply(a, b):
    product = [0] * (len(a) + len(b))
    for j in xrange(len(b) - 1, -1, -1):
        carry = 0
        for i in xrange(len(a) - 1, -1, -1):
            product[i + j + 1] += carry + (int(a[i]) * int(b[j]))
            carry = (product[i + j + 1]) / 10
            product[i + j + 1] %= 10
        product[j] += carry
    return ''.join(str(x) for x in product)


def SumOfListElement(list1):
    s = list1[0]
    for x in list1[1:]:
        add = [0] * (max(len(s), len(x)) + 1)
        l = len(add) - 1
        carry = 0
        for i, j in zip(range(len(s) - 1, -1, -1), range(len(x) - 1, -1, -1)):
            add[l] = carry + int(s[i]) + int(x[j])
            carry = add[l] / 10
            add[l] %= 10
            l = l - 1
        add[0] = carry
        s = ''.join(str(x) for x in add)
    return s


def splitMultiplicants(mul, length):
    return mul[:length], mul[length:]


def largeMultiply(a, b):
    if len(a) == 1 or len(b) == 1:
        return int(multiply(a, b))         

    m2 = (max(len(a), len(b)) / 2)

    A, B = splitMultiplicants(a, m2)
    C, D = splitMultiplicants(b, m2)
    
    AC = largeMultiply(A, C)
    PQ = largeMultiply(SumOfList(A, B), SumOfList(C, D))
    BD = largeMultiply(B, D)

    return (AC * pow(10, 2 * m2)) + (PQ - BD - AC) * pow(10, m2) + BD


def conventionalMatrixO3(t, k):
    szMtx = int(t[0])
    t = t[1:]
    k = k[1:]
    matrix1 = [[0 for x in range(szMtx)] for y in range(szMtx)] 
    matrix2 = [[0 for x in range(szMtx)] for y in range(szMtx)] 
    matrix3 = [[0 for x in range(szMtx)] for y in range(szMtx)] 
    for i in range(len(t)):
        matrix1[int(t[i][0]) - 1][int(t[i][1]) - 1] = list(t[i][2:])
        matrix2[int(k[i][0]) - 1][int(k[i][1]) - 1] = list(k[i][2:])

    for i in range(szMtx):
        for j in range(szMtx):
            dummyList = []
            for k in range(szMtx):
                dummyList.append((multiply(matrix1[i][k], matrix2[k][j])))
            matrix3[i][j] = SumOfListElement(dummyList)
    return matrix3


def strauss(t, k):
    szMtx = int(t[0])
    t = t[1:]
    k = k[1:]
    matrix1 = [[0 for x in range(szMtx)] for y in range(szMtx)] 
    matrix2 = [[0 for x in range(szMtx)] for y in range(szMtx)] 
    matrix3 = [[0 for x in range(szMtx)] for y in range(szMtx)] 
    for i in range(len(t)):
        matrix1[int(t[i][0]) - 1][int(t[i][1]) - 1] = list(t[i][2:])
        matrix2[int(k[i][0]) - 1][int(k[i][1]) - 1] = list(k[i][2:])


#===============================================================================
# SANDEEP - Code Start
# https://www.cheatography.com/walthered/cheat-sheets/pydev-shortcut-cheat-sheet/
#===============================================================================
def strauss_sandeep(t, k , MatrixSize):
    newSize = MatrixSize
#     print("T %d ",t)
#     print("T %d ",k)
    matrix1 = t
    matrix2 = k     
    # Converting String list to Int list to make calculation easy
    matrix1 = map(int, matrix1)
    matrix2 = map(int, matrix2)
#     print(matrix1)
#     print(matrix2)
    if(newSize > 1):
#         print(newSize)
        a11, a12, a21, a22 = splitMatrix(matrix1)
        b11, b12, b21, b22 = splitMatrix(matrix2)
        print("-------------------------------")
        print("a11 %d", a11)
        print("a12 %d", a12)
        print("a21 %d", a21)
        print("a22 %d", a22)
        print("b11 %d", b11)
        print("b12 %d", b12)
        print("b21 %d", b21)
        print("b22 %d", b22)     
        print("-------------------------------")
#------------------------------------------------------------
#     m1 = (a11+a22)(b11+b22)
#     m2 = (a21+a22)*b11
#     m3 = a11*(b12-b22)
#     m4 = a22*(b21-b11)
#     m5 = (a11+a12)*b22
#     m6 = (a21-a11)(b11+b12)
#     m7 = (a12-a22)(b21+b22)
#------------------------------------------------------------
#         print("addition(a11,a22) %d ",addition(a11,a22))
        m1 = strauss_sandeep(addition(a11, a22), addition(b11, b22), newSize / 2)
        m2 = strauss_sandeep(addition(a21, a22), b11 , newSize / 2)
        m3 = strauss_sandeep(substract(b12, b22), a11 , newSize / 2)
        m4 = strauss_sandeep(substract(b21, b11), a22, newSize / 2)
        m5 = strauss_sandeep(addition(a11, a12), b22, newSize / 2)
        m6 = strauss_sandeep(addition(b11, b12), substract(a21, a11), newSize / 2)
        m7 = strauss_sandeep(addition(b21, b22), substract(a12, a22), newSize / 2)
    
#===============================================================================
# #     c11 = m1+m4-m5+m7
# #     c12 = m3+m5
# #     c21 = m2+m4
# #     c22 = m1-m2+m3+m6
#===============================================================================
        c11 = addition(substract(addition(m1, m4), m5), m7)
        c12 = addition(m3, m5)
        c21 = addition(m2, m4)
        c22 = addition(substract(m1, m2), addition(m3, m6))
        # Matrix Multiplied
        return (c11 + c12 + c21 + c22)
    else:
        # Execute when size of matrix is one
#         print("1x1 :: Matrix")
        return multMat(matrix1, matrix2)
     

def splitMatrix(matrix1):
    list1 = matrix1[:len(matrix1) / 2]
    list2 = matrix1[len(matrix1) / 2:]
    a = list1 [:len(list1) / 2]
    b = list1 [len(list1) / 2:]
    c = list2 [:len(list2) / 2]
    d = list2 [len(list2) / 2:]
    return a, b, c, d

    
# multiply matrix
def multMat(matrix1, matrix2):
    multMat = [a * b for a, b in zip(matrix1, matrix2)]
    return multMat


# print any random matrix 
def printMatrix(matrix):
    print(matrix)


# Add two list
def addition(matrix1, matrix2):
    list = []
    for i in range (len(matrix1)):    
        temp = int(matrix1[i]) + int(matrix2[i])             
        list.append(temp)
    return list


# Subtract two list
def substract(matrix1, matrix2):
    substract = []
    for i in range (len(matrix1)):
        temp = int(matrix1[i]) - int(matrix2[i])    
        substract.append(temp)
    return substract
#===============================================================================
# SANDEEP - Code Ends
#===============================================================================


def SumOfList(list1, list2):
    return [str(int(x) + int(y)) for x, y in zip(list1, list2)]

        
def main(argv):
    t = []
    k = []
    with open(argv[1], 'r') as f, open('2' + argv[1], 'r') as w:
        for line in f:
            t.append("".join(c for c in line if c not in '(,) \n'))
        for line in w:
            k.append("".join(c for c in line if c not in '(,) \n'))
    # print conventionalMatrixO3(t,k)
    
#     Strassan Sandeep
    matrixSize = t[0]
    t = t[1:]
    k = k[1:]
    matrix1 = []
    matrix2 = []
    for i in range(len(t)): 
            temp = t[i]
            matrix1.append(temp[2:])
    for j in range(len(k)): 
            temp = k[j]
            matrix2.append(temp[2:])
#     print("T %d ",t)
    print(matrix1)
    print(matrix2)
    print strauss_sandeep(matrix1, matrix2 , int(matrixSize))

    
if __name__ == "__main__":
    main(sys.argv)
