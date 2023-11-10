import numpy as np
a=np.array([[1,2,3],[1,2,3],[1,2,3]])
b=np.array([[8,10,12],[8,10,12],[8,10,12]])
print("matrix a")
print(a)
print("matrix b")
print(b)

#matrix operations

print("Matrix a + matrix b ")
print(np.add(a,b))

print("Matrix b - matrix a ")
print(np.subtract(b,a))

print("Matrix a * matrix b ")
print(np.multiply(a,b))

print("Matrix b / matrix a ")
print(np.divide(b,a))

print("Matrix a . matrix b ")
print(np.dot(a,b))


print("Transpose of a ")
print(np.transpose(a))

#identity matrix

c=np.identity(3,dtype=int)
print("identity matrix of order 3")
print(c)

#one's matrix

d=np.ones([2,2])
print("ones matrix of order 2*2")
print(d)

#zero matrix

e=np.zeros([2,1])
print("zero matrix of order 2*1")
print(e)

#determinant

print("determinant of matrix a")
print(np.linalg.det(a))

#inverse

f=np.array([[4,3],[3,2]])
print("matrix f is:")
print(f)
print("inverse of matrix f")
print(np.linalg.inv(f))


