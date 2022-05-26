import scipy.misc
import matplotlib.pyplot

# This script demonstrates fancy indexing by setting values
# on the diagonals to 0.

# Load the Lena array
lena = scipy.misc.ascent()
xmax = lena.shape[0]
ymax = lena.shape[1]

# Fancy indexing
# Set values on diagonal to 0
# 对角线设置为零。
# x 0-xmax
# y 0-ymax
lena[range(xmax), range(ymax)] = 0

# Set values on other diagonal to 0
# 另一条对角线设置为零。
# x xmax-0
# y 0-ymax
lena[range(xmax-1,-1,-1), range(ymax)] = 0

# Plot Lena with diagonal lines set to 0
matplotlib.pyplot.imshow(lena)
matplotlib.pyplot.show()
