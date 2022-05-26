import numpy as np
import sys

# 调用mat函数创建矩阵：
# Singular matrix
# A = np.mat('1 2 3; 4 5 6; 7 8 9')
A = np.mat('3 2 3; 4 5 6; 7 8 9')
print("Creation from string", A)
# 用T属性获取转置矩阵：
print("transpose A", A.T)
# 用I属性获取逆矩阵：
print("Inverse A", A.I)
# 使用NumPy数组进行创建：
print("Creation from array",
	np.mat(np.arange(9).reshape(3, 3)))


