import numpy as np
x = np.arange(-9, 9)
y = -x
# 当两个操作数的符号不一致时，XOR操作的结果为负数。
print("Sign different?", (x ^ y) < 0)
print("Sign different?", np.less(np.bitwise_xor(x, y), 0))
# 如果我们在2的幂数以及比它小1的数之间执行位与操作AND，那么应该得到0。
print("Power of 2?\n", x, "\n", (x & (x - 1)) == 0)
print("Power of 2?\n", x, "\n", np.equal(np.bitwise_and(x, (x - 1)), 0))
# 二进制的位左移一位，则数值翻倍。
print("Modulus 4\n", x, "\n", x & ((1 << 2) - 1))
print("Modulus 4\n", x, "\n", np.bitwise_and(x, np.left_shift(1, 2) - 1))

