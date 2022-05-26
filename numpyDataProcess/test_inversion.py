import numpy as np
# 使用mat函数创建示例矩阵
A = np.mat("0 1 2;1 0 3;4 -3 8")
print("A\n", A)
# 使用inv函数计算逆矩阵
inverse = np.linalg.inv(A)
print("inverse of A\n", inverse)
# 检查一下原矩阵和求得的逆矩阵相乘的结果
print("Check\n", A * inverse)
