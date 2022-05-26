import numpy as np 
from datetime import datetime 

import numpy as np 
import sys 
h, l, c = np.loadtxt('data.csv', delimiter=',', usecols=(4, 5, 6), unpack=True) 

# ATR是基于N个交易日的最高价和最低价进行计算的
N = int(sys.argv[1]) 
h = h[-N:] 
l = l[-N:]

# 我们还需要知道前一个交易日的收盘价。
previousclose = c[-N -1: -1]

# h – l 当日股价范围，即当日最高价和最低价之差。
# h – previousclose 当日最高价和前一个交易日收盘价之差。
# previousclose – l 前一个交易日收盘价和当日最低价之差。
# 真实波动幅度，也就是这三者的最大值。
truerange = np.maximum(h - l, h - previousclose, previousclose - l)
# 数组的首个元素就是truerange数组元素的平均值。
atr = np.zeros(N)
atr[0] = np.mean(truerange)
# 用公式计算其他元素的值
for i in range(1, N): 
	atr[i] = (N - 1) * atr[i - 1] + truerange[i] 
	atr[i] /= N

print("ATR", atr)