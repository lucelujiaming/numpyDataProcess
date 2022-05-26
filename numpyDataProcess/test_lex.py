import numpy as np 
import datetime 
def datestr2num(s): 
    return datetime.datetime.strptime(s.decode("ascii"), "%d-%m-%Y").toordinal() 
# 载入收盘价和日期数据。
dates,closes=np.loadtxt('AAPL.csv', delimiter=',', usecols=(1, 6), 
    converters={1:datestr2num}, unpack=True) 
# 使用lexsort函数按照收盘价排序：
indices = np.lexsort((dates, closes)) 
print("Indices", indices)
print(["%s %s" % (datetime.date.fromordinal(
    int(dates[i])), closes[i]) for i in indices])


