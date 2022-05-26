import numpy as np 
from matplotlib.pyplot import plot 
from matplotlib.pyplot import show 
import sys 
# 将函数值初始化为0
t = np.linspace(-np.pi, np.pi, 201) 
k = np.arange(1, float(sys.argv[1])) 
f = np.zeros_like(t) 
# 直接使用sin和sum函数进行计算
for i in range(len(t)): 
	f[i] = np.sum(np.sin(2 * np.pi * k * t[i])/k) 
f = (-2 / np.pi) * f 
# 使用如下代码绘制波形
plot(t, f, lw=1.0) 
plot(t, np.abs(f), lw=2.0) 
show()




