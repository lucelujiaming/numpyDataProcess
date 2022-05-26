import numpy as np
# 创建一个矩阵
A = np.mat("3 -2;1 0")
print("A\n", A)
# 调用eigvals函数求解特征值
print("Eigenvalues", np.linalg.eigvals(A))
# 使用eig函数求解特征值和特征向量。
eigenvalues, eigenvectors = np.linalg.eig(A)
print("First tuple of eig", eigenvalues)
print("Second tuple of eig\n", eigenvectors)
# 使用dot函数验证求得的解是否正确。
for i in range(len(eigenvalues)):
    print("Left", np.dot(A, eigenvectors[:,i]))
    print("Right", eigenvalues[i] * eigenvectors[:,i])

