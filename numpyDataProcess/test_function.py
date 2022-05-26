# coding: utf-8
import numpy as np

i2 = np.eye(2) 
print(i2)
np.savetxt("eye.txt", i2)

c,v=np.loadtxt('data.csv', 
	# 设置分隔符为,（英文标点逗号）
	delimiter=',', 
	# 获取第7字段至第8字段的数据，
	# 也就是股票的收盘价和成交量数据。
	usecols=(6,7), 
	# 分拆存储不同列的数据，
	# 即分别将收盘价和成交量的数组赋值给变量c和v。
	unpack=True)
# 计算成交量加权平均价格
vwap = np.average(c, weights=v) 
print("VWAP =", vwap)
print("mean =", np.mean(c))
# 计算时间加权平均价格
# 用arange函数创建一个从0开始依次增长的自然数序列，自然数的个数即为收盘价的个数。
t = np.arange(len(c))
print("twap =", np.average(c, weights=t))

# 将每日最高价和最低价的数据载入数组：
h,l=np.loadtxt('data.csv',delimiter=',', usecols=(4,5), unpack=True)
# 获取价格区间：
print("highest =", np.max(h)) 
print("lowest =", np.min(l))
print("middle =", (np.max(h) + np.min(l)) /2)
# 计算数组的取值范围。该函数返回的是数组元素的最大值和最小值之间的差值。
print("Spread high price", np.ptp(h))
print("Spread low price", np.ptp(l))






