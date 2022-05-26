from scipy.io import wavfile 
import matplotlib.pyplot as plt 
# import urllib2 
import urllib.request
import numpy as np 
import sys 

import ssl
ssl._create_default_https_context = ssl._create_unverified_context

response = urllib.request.urlopen('http://www.thesoundarchive.com/austinpowers/smashingbaby.wav') 
print(response.info())
WAV_FILE = 'smashingbaby.wav' 
# TypeError: write() argument must be str, not bytes
# 使用二进制方式打开就不会出现这个问题。
filehandle = open(WAV_FILE, 'wb+') 
# 使用scipy.io.wavfile模块中的read函数可以将该文件转换为一个NumPy数组。
filehandle.write(response.read()) 
filehandle.close() 
# 使用read函数读入文件
sample_rate, data = wavfile.read(WAV_FILE) 
print("Data type", data.dtype, "Shape", data.shape)
plt.subplot(2, 1, 1) 
plt.title("Original" ) 
plt.plot(data) 
plt.subplot(2, 1, 2) 
# 重复音频片段
repeated = np.tile(data, int(sys.argv[1])) 
# 绘制音频数据
plt.title("Repeated") 
plt.plot(repeated) 
wavfile.write("repeated_yababy.wav", sample_rate, repeated) 
plt.show ()
