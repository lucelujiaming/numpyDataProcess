import numpy as np
a = np.arange(9)
# 沿着指定的轴，在连续的数组元素之间递归调用通用函数。
print("Reduce", np.add.reduce(a))
# accumulate方法同样可以递归作用于输入数组。
print("Accumulate", np.add.accumulate(a))
# 按照列表执行reduce操作。
print("Reduceat", np.add.reduceat(a, [0, 5, 2, 7]))
# 下面是reduceat的步骤。
# 对数组中索引值在0到5之间的元素进行reduce操作。
print("Reduceat step I", np.add.reduce(a[0:5]))
# 直接返回索引值为5的元素
print("Reduceat step II", a[5])
# 对索引值在2到7之间的数组元素进行reduce操作。
print("Reduceat step III", np.add.reduce(a[2:7]))
# 对索引值从7开始直到数组末端的元素进行reduce操作。
print("Reduceat step IV", np.add.reduce(a[7:]))
# 作用于两个输入数组之间存在的所有元素对。
print("Outer", np.add.outer(np.arange(3), a))
