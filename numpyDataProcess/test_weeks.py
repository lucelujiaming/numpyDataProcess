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
    return datetime.strptime(s.decode("ascii"), "%d-%m-%Y").date().weekday() 
dates, open, high, low, close=np.loadtxt(
    'data.csv', delimiter=',', usecols=(1, 3, 4, 
    5, 6), converters={1: datestr2num}, unpack=True)
# 只考虑前三周的数据
close = close[:16] 
dates = dates[:16]
# 找到第一个星期一。因为星期一是0，因此上只需要展平后取0个元素。
first_monday = np.ravel(np.where(dates == 0))[0] 
print("The first Monday index is", first_monday)
# 下面要做的是找到示例数据的最后一个星期五。
# 方法同上，展平后取-1个元素。
# 找到最后一个星期五
last_friday = np.ravel(np.where(dates == 4))[-1] 
print("The last Friday index is", last_friday)
# 存储三周内每一天的索引值。
weeks_indices = np.arange(first_monday, last_friday + 1) 
print("Weeks indices initial", weeks_indices)
# 每个子数组5个元素，用split函数切分数组：
# 一共15个元素，每个子数组5个元素，需要分成3组。
weeks_indices = np.split(weeks_indices, 3) 
print("Weeks indices after split", weeks_indices)

def summarize(a, o, h, l, c): 
    monday_open = o[a[0]] 
    week_high = np.max( np.take(h, a) ) 
    week_low = np.min( np.take(l, a) )
    friday_close = c[a[-1]] 
    return("APPL", monday_open, week_high, week_low, friday_close)

# apply_along_axis函数会调用另外一个由我们给出的函数，
# 作用于每一个数组元素上。
weeksummary = np.apply_along_axis(
    summarize, 1, weeks_indices,open, high, low, close) 
print("Week summary", weeksummary)
# 将数据保存至文件。
np.savetxt("weeksummary.csv", weeksummary, delimiter=",", fmt="%s")







