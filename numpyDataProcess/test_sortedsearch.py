import numpy as np 
# 需要一个排序后的数组。
a = np.arange(5) 
# 调用searchsorted函数：
indices = np.searchsorted(a, [-2, 7]) 
print("Indices", indices)
# 使用insert函数构建完整的数组。
print("The full array", np.insert(a, indices, [-2, 7]))

a = np.arange(7) 
# 生成选择偶数元素的条件变量
condition = (a % 2) == 0 
# 使用extract函数基于生成的条件从数组中抽取元素
print("Even numbers", np.extract(condition, a))
# 使用nonzero函数抽取数组中的非零元素
print("Non zero", np.nonzero(a))
