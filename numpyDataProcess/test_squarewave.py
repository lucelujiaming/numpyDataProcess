import numpy as np 
from matplotlib.pyplot import plot 
from matplotlib.pyplot import show 
import sys 
# 从初始化t和k开始，并将函数值初始化为0
t = np.linspace(-np.pi, np.pi, 201) 
k = np.arange(1, float(sys.argv[1])) 
k = 2 * k - 1 
f = np.zeros_like(t) 
# 直接使用sin和sum函数进行计算
for i in range(len(t)): 
    f[i] = np.sum(np.sin(k * t[i])/k) 
f = (4 / np.pi) * f 
# 绘制波形
plot(t, f) 
show()

