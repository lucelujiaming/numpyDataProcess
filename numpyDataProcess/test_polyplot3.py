import numpy as np 
import matplotlib.pyplot as plt 
# 创建多项式函数及其导函数。
func = np.poly1d(np.array([1, 2, 3, 4]).astype(float)) 
x = np.linspace(-10, 10, 30) 
y = func(x) 
func1 = func.deriv(m=1) 
y1 = func1(x) 
func2 = func.deriv(m=2) 
y2 = func2(x) 

# 使用subplot函数创建第一个子图。
# 该函数的第一个参数是子图的行数，这里是3
# 第二个参数是子图的列数，这里是1
# 第三个参数是一个从1开始的序号。这里是1
plt.subplot(3, 1, 1) 
# 或者写成：
# plt.subplot(311)
# 使用红色实线绘制。
plt.plot(x, y, 'r-' ) 
# 设置子图的标题为Polynomial，
plt.title("Polynomial")

# 创建第二个子图。
plt.subplot(3, 1, 2) 
# 使用蓝色三角形绘制。
plt.plot(x, y1, 'b^') 
# 设置子图的标题为First Derivative。
plt.title("First Derivative") 

# 创建第三个子图。
plt.subplot(3, 1, 3) 
# 使用绿色圆形绘制。
plt.plot(x, y2, 'go') 
# 设置子图的标题为Second Derivative。
plt.title("Second Derivative") 

plt.xlabel('x') 
plt.ylabel('y') 
plt.show()

