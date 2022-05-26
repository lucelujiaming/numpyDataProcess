import numpy as np
a = np.arange(-4, 4)
# 逐个返回两个数组中元素相除后的余数。
print("Remainder", np.remainder(a, 2))
print("Mod", np.mod(a, 2))
print("% operator", a % 2)
print("Fmod", np.fmod(a, 2))


