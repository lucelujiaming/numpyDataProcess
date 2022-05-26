import numpy as np 
A = np.mat("3 4;5 6") 
print("A : ", A)
# 使用det函数计算行列式
print("Determinant", np.linalg.det(A))
