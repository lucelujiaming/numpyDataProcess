import numpy as np
# 创建一个矩阵
A = np.mat("4 11 14;8 7 -2")
print("A : ", A)
# 使用svd函数分解矩阵
# 得到的结果包含等式中左右两端的两个正交矩阵U和V，
# 以及中间的奇异值矩阵Sigma
U, Sigma, V = np.linalg.svd(A, full_matrices=False)
print("U", U)
print("Sigma", Sigma)
print("V", V)
# 使用diag函数生成完整的奇异值矩阵。将分解出的3个矩阵相乘。
print("Product\n", U * np.diag(Sigma) * V)