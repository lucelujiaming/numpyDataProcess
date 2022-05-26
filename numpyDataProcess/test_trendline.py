# coding: utf-8
import numpy as np 
import sys 

from matplotlib import pyplot as plt
# 支持中文
plt.rcParams['font.family'] = ['Songti SC']  # 用来正常显示中文标签
plt.rcParams['axes.unicode_minus'] = False  # 用来正常显示负号

# 定义一个函数用直线y= at + b来拟合数据，该函数应返回系数a和b。
def fit_line(t, y): 
    # 用到linalg包中的lstsq函数。将直线方程重写为y = Ax的形式。
    A = np.vstack([t, np.ones_like(t)]).T 
    return np.linalg.lstsq(A, y)[0] 

h, l, c = np.loadtxt('data.csv', delimiter=',' , usecols=(4, 5, 6), unpack=True) 
# 确定枢轴点的位置。这里，我们假设它们等于最高价、最低价和收盘价的算术平均值。
pivots = (h + l + c ) / 3 
print("Pivots", pivots)
t = np.arange(len(c)) 
# 假设支撑位在枢轴点下方一个当日股价区间的位置，
sa, sb = fit_line(t, pivots - (h - l)) 
# 而阻力位在枢轴点上方一个当日股价区间的位置，据此拟合支撑位和阻力位的趋势线。
ra, rb = fit_line(t, pivots + (h - l)) 
support = sa * t + sb 
resistance = ra * t + rb 
# 检查一下有多少个数据点落在支撑位和阻力位之间。
condition = (c > support) & (c < resistance) 
print("Condition", condition)
# 设置一个判断数据点是否位于趋势线之间的条件，作为where函数的参数。
between_bands = np.where(condition) 
# 复查一下具体取值：
print("support[between_bands] : ", support[between_bands])
print("c[between_bands] : ", c[between_bands])
print("resistance[between_bands] : ", resistance[between_bands])
# where函数返回的是一个秩为2的数组，因此在使用len函数之前需要调用ravel函数。
between_bands = len(np.ravel(between_bands))
print("Number points between bands", between_bands)
print("Ratio between bands", float(between_bands)/len(c))
# 我们还得到了一个额外的奖励：一个新的预测模型。
print("Tomorrows support", sa * (t[-1] + 1) + sb)
print("Tomorrows resistance", ra * (t[-1] + 1) + rb)
a1 = c[c > support] 
a2 = c[c < resistance] 
# 用intersect1d函数计算两者相交的结果。
print("Number of points between bands 2nd approach" ,
    len(np. intersect1d(a1, a2)))
# 再次将结果绘制出来
plt.plot(t, c) 
plt.plot(t, support) 
plt.plot(t, resistance) 
plt.show()

