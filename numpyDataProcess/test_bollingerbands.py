# coding: utf-8
import numpy as np 
import sys 

from matplotlib import pyplot as plt
# 支持中文
plt.rcParams['font.family'] = ['Songti SC']  # 用来正常显示中文标签
plt.rcParams['axes.unicode_minus'] = False  # 用来正常显示负号

# 简单移动平均线可以用信号处理技术求解——与1/N的权重进行卷积运算
N = int(sys.argv[1]) 
weights = np.ones(N) / N 
print("Weights", weights)
c = np.loadtxt('data.csv', delimiter=',', usecols=(6,), unpack=True) 
# 使用这些权重值，调用convolve函数
# 简单移动平均线就是布林带的中轨。
sma = np.convolve(weights, c)[N-1:-N+1]

# 遍历和这些权重值有关的数据子集。计算其标准差。
# 我们从convolve函数返回的数组中，取出中间的长度为N的部分
deviation = [] 
C = len(c) 
for i in range(N - 1, C): 
	# 如果可以从当前位置获取N个元素。就直接获取。
	if i + N < C: 
		dev = c[i: i + N] 
	# 否则获取最后N个元素。
	else: 
		dev = c[-N:] 
	averages = np.zeros(N) 
	# fill函数可以构建元素值完全相同的数组。
	averages.fill(sma[i - N - 1]) 
	# 计算其标准方差。
	dev = dev - averages 
	dev = dev ** 2 
	dev = np.sqrt(np.mean(dev)) 
	deviation.append(dev)
# 标准方差的平方就是标准差。
deviation = 2 * np.array(deviation) 
print(len(deviation), len(sma))
# 计算布林带的上轨和下轨。
upperBB = sma + deviation 
lowerBB = sma - deviation 

c_slice = c[N-1:] 
print("c_slice : ", c_slice)
between_bands = np.where((c_slice < upperBB) & (c_slice > lowerBB)) 
print("between_bands : ", between_bands)
print("lowerBB[between_bands] : ", lowerBB[between_bands])
print("c[between_bands] : ", c[between_bands])
print("upperBB[between_bands] : ", upperBB[between_bands]) 
between_bands = len(np.ravel(between_bands)) 
print("Ratio between bands", float(between_bands)/len(c_slice))

# 使用如下代码绘制布林带
t = np.arange(N - 1, C) 
plt.plot(t, c_slice, lw=1.0) 
plt.plot(t, sma, lw=2.0) 
plt.plot(t, upperBB, lw=3.0) 
plt.plot(t, lowerBB, lw=4.0) 
plt.show()