import numpy as np

a = np.arange(5)
print("a =", a)
# 将所有比给定最大值还大的元素全部设为给定的最大值，
# 而所有比给定最小值还小的元素全部设为给定的最小值。
print("Clipped", a.clip(1, 2))

a = np.arange(4)
print(a)
# 返回一个根据给定条件筛选后的数组。
print("Compressed", a.compress(a > 2))

b = np.arange(1, 9)
print("b =", b)
# 计算数组中所有元素的乘积。
print("Factorial", b.prod())
# 计算数组元素的累积乘积。
print("Factorials", b.cumprod())
