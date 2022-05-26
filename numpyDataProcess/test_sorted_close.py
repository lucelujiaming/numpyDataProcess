# coding: utf-8
import numpy as np

# 动手实践：简单统计分析
c=np.loadtxt('data.csv', delimiter=',', usecols=(6,), unpack=True)
print("median =", np.median(c))
# 对价格数组进行排序
sorted_close = np.msort(c) 
print("sorted =", sorted_close)
# 并输出排序后居于中间位置的值。
N = len(c) 
print("middle =", sorted_close[int((N - 1)/2)])
# 对于长度为偶数的数组，中位数的值应该等于中间那两个数的平均值。因此，输入如下代码：
print("average middle =", 
	(sorted_close[int(N /2)] + sorted_close[int((N - 1) / 2)]) / 2)
# 另外一个我们关心的统计量就是方差。
print("variance =", np.var(c))

