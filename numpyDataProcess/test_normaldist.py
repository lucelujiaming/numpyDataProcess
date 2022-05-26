import numpy as np 
import matplotlib.pyplot as plt 

N=10000 
# 使用NumPy random模块中的normal函数产生指定数量的随机数。
normal_values = np.random.normal(size=N) 
# 绘制分布直方图和理论上的概率密度函数（均值为0、方差为1的正态分布）曲线。
dummy, bins, dummy = plt.hist(normal_values, bins=30, lw=1) 
sigma = 1 
mu = 0 
plt.plot(bins, 1/(sigma * np.sqrt(2 * np.pi)) 
		* np.exp( - (bins -mu)**2 / (2 * sigma**2) ),lw=2) 
plt.show()