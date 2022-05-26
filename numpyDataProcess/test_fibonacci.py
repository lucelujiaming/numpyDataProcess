import numpy as np 
# 创建斐波那契矩阵
F = np.matrix([[1, 1], [1, 0]]) 
print("F : ", F)
# 计算斐波那契数列中的第8个数，即矩阵的幂为8减去1
print("8th Fibonacci : ", (F ** 7)[0, 0])
# 利用黄金分割公式计算斐波那契数。
n = np.arange(1, 9) 
sqrt5 = np.sqrt(5) 
phi = (1 + sqrt5)/2 
fibonacci = np.rint((phi**n - (-1/phi)**n)/sqrt5) 
print("Fibonacci : ", fibonacci)
