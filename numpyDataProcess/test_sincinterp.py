import numpy as np 
from scipy import interpolate 
import matplotlib.pyplot as plt 
# 创建数据点并添加噪音
x = np.linspace(-18, 18, 36) 
noise = 0.1 * np.random.random(len(x)) 
signal = np.sinc(x) + noise 
# 创建一个线性插值函数，并应用于有5倍数据点个数的输入数组
interpreted = interpolate.interp1d(x, signal)
x2 = np.linspace(-18, 18, 180) 
y = interpreted(x2) 
# 使用三次插值。
cubic = interpolate.interp1d(x, signal, kind="cubic") 
y2 = cubic(x2) 
# 绘制结果。
plt.plot(x, signal, 'o', label="data") 
plt.plot(x2, y, '-', label="linear") 
plt.plot(x2, y2, '-', lw=2, label="cubic" ) 
plt.legend() 
plt.show()