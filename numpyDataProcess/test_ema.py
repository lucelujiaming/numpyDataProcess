# coding: utf-8
import numpy as np 
import sys 

from matplotlib import pyplot as plt
# 支持中文
plt.rcParams['font.family'] = ['Songti SC']  # 用来正常显示中文标签
plt.rcParams['axes.unicode_minus'] = False  # 用来正常显示负号

x = np.arange(5) 
# exp函数可以计算出每个数组元素的指数
print("Exp", np.exp(x))
# 返回一个元素值在指定的范围内均匀分布的数组
print("Linspace", np.linspace(-1, 0, 5))
# 下面我们来对示例数据计算指数移动平均线。
# (1) 还是回到权重的计算——这次使用exp和linspace函数。
N = int(sys.argv[1]) 
weights = np.exp(np.linspace(-1., 0., N)) 
# (2) 对权重值做归一化处理。我们将用到ndarray对象的sum方法。
weights /= weights.sum() 
print("Weights", weights)
# 要使用在简单移动平均线一节中学习到的convolve函数即可。
c = np.loadtxt('data.csv', delimiter=',', usecols=(6,), unpack=True) 
ema = np.convolve(weights, c)[N-1:-N+1] 
# 同样，我们还是将结果绘制出来。
t = np.arange(N - 1, len(c)) 
plt.plot(t, c[N-1:], lw=1.0) 
plt.plot(t, ema, lw=2.0) 
plt.show()

