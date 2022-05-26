# coding: utf-8
import numpy as np 
import sys 

from matplotlib import pyplot as plt
# 支持中文
plt.rcParams['font.family'] = ['Songti SC']  # 用来正常显示中文标签
plt.rcParams['axes.unicode_minus'] = False  # 用来正常显示负号

# 简单移动平均线可以用信号处理技术求解——与1/N的权重进行卷积运算
# 创建一个长度为N的元素均初始化为1的数组
N = int(sys.argv[1]) 
# 对整个数组除以N，即可得到权重。
weights = np.ones(N) / N
print("Weights", weights)
# 使用这些权重值，调用convolve函数
c = np.loadtxt('data.csv', delimiter=',', usecols=(6,), unpack=True) 
# 我们从convolve函数返回的数组中，取出中间的长度为N的部分
sma = np.convolve(weights, c)[N-1:-N+1]
# 创建一个存储时间值的数组，
t = np.arange(N - 1, len(c)) 
# 并使用Matplotlib进行绘图。
plt.plot(t, c[N-1:], lw=1.0) 
plt.plot(t, sma, lw=2.0) 
plt.show()
