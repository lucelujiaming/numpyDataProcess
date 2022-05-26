# coding: utf-8
import numpy as np 
import sys 

from matplotlib import pyplot as plt
# 支持中文
plt.rcParams['font.family'] = ['Songti SC']  # 用来正常显示中文标签
plt.rcParams['axes.unicode_minus'] = False  # 用来正常显示负号

N = int(sys.argv[1]) 
c = np.loadtxt('data.csv', delimiter=',', usecols=(6,), unpack=True)

# 获取一个包含N个股价的向量b。
b = c[-N:] 
b = b[::-1] 
print("b", b)
# 初始化一个N×N的二维数组A，元素全部为0。
A = np.zeros((N, N), float) 
# 用b向量中的N个股价值填充数组A。
print("Zeros N by N", A)
for i in range(N): 
	A[i, ] = c[-N - 1 - i: - 1 - i] 
print("A", A)
# 确定线性模型中的那些系数，以解决最小平方和的问题。
# 返回的元组中包含稍后要用到的系数向量x、一个残差数组、A的秩以及A的奇异值。
(x, residuals, rank, s) = np.linalg.lstsq(A, b) 
print("x, residuals, rank, s : ", x, residuals, rank, s)
# 一旦得到了线性模型中的系数，我们就可以预测下一次的股价了。
# 使用NumPy中的dot函数计算系数向量与最近N个价格构成的向量的点积（dot product）。
print("np.dot(b, x) : ",  np.dot(b, x))
