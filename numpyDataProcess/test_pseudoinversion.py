import numpy as np
# 创建一个矩阵
A = np.mat("4 11 14;8 7 -2")
print("A ：", A)
# 使用pinv函数计算广义逆矩阵
pseudoinv = np.linalg.pinv(A)
print("Pseudo inverse : ", pseudoinv)
# 将原矩阵和得到的广义逆矩阵相乘
print("Check : ", A * pseudoinv)
