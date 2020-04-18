import numpy as np
import matplotlib.pyplot as plt
from scipy.signal import find_peaks

def sinWave(t_axis, freq, amp):
    return amp * np.sin(2*np.pi*freq*t_axis)

N = 1000                   ## number of sampling points
fs = 1e3                   ## sampling frequency
dt = 1/fs                  ## spacing between two time on axis
df = fs/N                  ## spacing between two freqencies on axis

t_axis = np.arange(N)*dt
f_axis = np.arange(N)*df

y1 = sinWave(t_axis,1,2)
y2 = sinWave(t_axis,21,4)
y3 = sinWave(t_axis,5,5)
y4 = sinWave(t_axis,13,6)

y = y1 + y2 + y3 + y4

yf = abs(np.fft.fft(y))
# yfs = np.fft.fftshift(yf)     	## shift 0 frequency to middle
                                	## [0,1,2,3,4,-4,-3,-2,-1] -> [-4,-3,-2,-1,0,1,2,3,4]
                                    ##                 (0, fs) -> (-fs/2, fs/2)
                                	## just plot the positive frequency, so dont need to shift

yfn = yf * 2 / N		        	## normalization
									## let the amplitude of output signal equals to inputs

plt.figure('Title', figsize=(6,6))

plt.subplot(311)
plt.plot(t_axis,y1)
plt.plot(t_axis,y2)
plt.plot(t_axis,y3)
plt.plot(t_axis,y4)

plt.title('Original')
plt.xlabel('time (t)')


plt.subplot(312)
plt.plot(t_axis,y,'b')

plt.title('Mix')
plt.xlabel('time (t)')


plt.subplot(313)

# maxFreq = (N//2)*df
maxFreq = 100
maxFreqIndex = int(maxFreq/df)

plt.plot(f_axis[:maxFreqIndex],yfn[:maxFreqIndex],'r')

peaks, _ = find_peaks(yfn[:maxFreqIndex], height = 1)
plt.plot(peaks*df, yfn[peaks], 'x')

ybegin,yend = plt.ylim()
plt.yticks(range(int(ybegin),int(yend)+1,1))
plt.xticks(f_axis[:maxFreqIndex:5])
plt.title('FFT')
plt.xlabel('freq (Hz)')

plt.subplots_adjust(hspace=0.7)
plt.show()
