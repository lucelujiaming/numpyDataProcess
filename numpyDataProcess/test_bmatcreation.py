import numpy as np
# 创建一个2×2的单位矩阵
A = np.eye(2)
# 创建另一个与A同型的矩阵，并乘以2：
print("A", A)
B = 2 * A
print("B", B)
print("Compound matrix\n", np.bmat("A B; A B"))

