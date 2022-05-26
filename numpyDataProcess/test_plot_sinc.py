import numpy as np 
from matplotlib.pyplot import plot, show, legend 
from matplotlib.dates import datestr2num 
import sys 
# 生成一组均匀分布的数值。
x = np.linspace(0, 4, 100)
# 调用i0函数进行计算
vals = np.i0(x) 
valsSinc = np.sinc(x)
# 绘制修正的贝塞尔函数：
plot(x, vals) 
plot(x, valsSinc) 
show()

