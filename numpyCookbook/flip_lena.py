import scipy.misc
import matplotlib.pyplot

# Load the Lena array
lena = scipy.misc.ascent()

# Plot the Lena array
matplotlib.pyplot.subplot(221)
matplotlib.pyplot.imshow(lena)

#Plot the flipped array
matplotlib.pyplot.subplot(222)
matplotlib.pyplot.imshow(lena[:,::-1])

#Plot a slice array
matplotlib.pyplot.subplot(223)
# 显示左上角四分之一。
matplotlib.pyplot.imshow(lena[:lena.shape[0]//2,:lena.shape[1]//2])

# Apply a mask
# 找到数组中的偶数，之后把他们全部设置为零。
mask = lena % 2 == 0
masked_lena = lena.copy()
masked_lena[mask] = 0
matplotlib.pyplot.subplot(224)
matplotlib.pyplot.imshow(masked_lena)

matplotlib.pyplot.show()
