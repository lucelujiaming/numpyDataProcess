import numpy as np 
import matplotlib.pyplot as plt 
# 以自然数序列作为多项式的系数，使用poly1d函数创建多项式。
funcPoly = np.poly1d(np.array([1, 2, 3, 4]).astype(float)) 
print("funcPoly \n", funcPoly)
funcX2  = np.poly1d(np.array([0, 1, 0, 0]).astype(float)) 
print("funcX2 : \n", funcX2)
# 在-10和10之间产生30个均匀分布的值。
x = np.linspace(-10, 10, 30) 
# 计算我们在第一步中创建的多项式的值。
yPoly = funcPoly(x) 
yX2   = funcX2(x) 
# 调用plot函数
plt.plot(x, yPoly) 
plt.plot(x, yX2) 
# 添加x轴标签。
plt.xlabel('x') 
# 数添加y轴标签。
plt.ylabel('y(x)') 
# 调用show函数显示函数图像。
plt.show()