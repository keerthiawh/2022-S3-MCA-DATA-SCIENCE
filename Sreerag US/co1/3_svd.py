import numpy as np
#single value decomposition

a=np.array([[3,4],[5,7]])
print("Matrix is:")
print(a)
m,n,p=np.linalg.svd(a)
print("single value decomposition of Array:")
print()
print(m)
print()
print(n)
print()
print(p)

#remake

print("Remake")
b=(m@np.diag(n)@p)
print(b)

