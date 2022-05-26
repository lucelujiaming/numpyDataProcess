import numpy as np
from datetime import datetime

# 星期一 0 
# 星期二 1 
# 星期三 2 
# 星期四 3 
# 星期五 4 
# 星期六 5 
# 星期日 6 
def datestr2num(s): 
	return datetime.strptime(s.decode("ascii"), 
		"%d-%m-%Y").date().weekday()

dates, close=np.loadtxt('data.csv', delimiter=',', usecols=(1,6), 
	converters={1:datestr2num}, unpack=True) 
print("Dates =", dates)

# 创建一个包含5个元素的数组，分别代表一周的5个工作日。
# 保存各工作日的平均收盘价。
averages = np.zeros(5)

# 遍历0到4的日期标识，或者说是遍历星期一到星期五，
# 然后用where函数得到各工作日的索引值并存储在indices数组中。
for i in range(5): 
	indices = np.where(dates == i) 
	prices = np.take(close, indices) 
	avg = np.mean(prices) 
	print("Day", i, "prices", prices, "Average", avg)
	averages[i] = avg

# 找出哪个工作日的平均收盘价是最高的，哪个是最低的。
top = np.max(averages) 
print("Highest average", top)
print("Top day of the week", np.argmax(averages))

bottom = np.min(averages) 
print("Lowest average", bottom)
print("Bottom day of the week", np.argmin(averages))

