# coding: utf-8
import numpy as np 
import sys 

from matplotlib import pyplot as plt
# 支持中文
plt.rcParams['font.family'] = ['Songti SC']  # 用来正常显示中文标签
plt.rcParams['axes.unicode_minus'] = False  # 用来正常显示负号

# 从CSV文件（本章示例代码文件夹中）中读入两只股票的收盘价数据，
bhp = np.loadtxt('BHP.csv', delimiter=',', usecols=(6,), unpack=True)
# 并计算收益率。
bhp_returns = np.diff(bhp) / bhp[ : -1]
vale = np.loadtxt('VALE.csv', delimiter=',', usecols=(6,), unpack=True)
vale_returns = np.diff(vale) / vale[ : -1]

# 协方差描述的是两个变量共同变化的趋势，其实就是归一化前的相关系数。
covariance = np.cov(bhp_returns, vale_returns)
print("Covariance", covariance)
# 使用diagonal函数查看对角线上的元素
print("Covariance diagonal", covariance.diagonal())
# 使用trace函数计算矩阵的迹，即对角线上元素之和。
print("Covariance trace", covariance.trace())
# 两个向量的相关系数被定义为协方差除以各自标准差的乘积。
print(covariance/ (bhp_returns.std() * vale_returns.std()))
# 我们将用相关系数来度量这两只股票的相关程度。
print("Correlation coefficient", np.corrcoef(bhp_returns, vale_returns))
# 计算这两只股票收盘价的差值，以判断是否同步：
difference = bhp - vale
# 检查最后一次收盘价是否在同步状态
avg = np.mean(difference)
dev = np.std(difference)
print("Out of sync", np.abs(difference[-1] - avg) > 2 * dev)
# 使用如下代码进行绘图
t = np.arange(len(bhp_returns))
plt.plot(t, bhp_returns, lw=1)
plt.plot(t, vale_returns, lw=2)
plt.show()