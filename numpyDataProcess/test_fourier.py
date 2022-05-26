import numpy as np 
from matplotlib.pyplot import plot, show 
# 创建一个包含30个点的余弦波信号
x = np.linspace(0, 20 * np.pi, 300) 
wave = np.cos(x) 
# 使用fft函数对余弦波信号进行傅里叶变换。
transformed = np.fft.fft(wave) 
# 对变换后的结果应用ifft函数，应该可以近似地还原初始信号。
print("np.all : ", 
	np.all(np.abs(np.fft.ifft(transformed) - wave) < 10 ** -9))
# 绘制变换前的信号。
plot(x) 
plot(wave) 
# 绘制变换后的信号。
plot(transformed) 
show()