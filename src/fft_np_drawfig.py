import numpy as np
import matplotlib.pyplot as plt

t_axis = np.linspace(0, 5, 51)
f_axis = np.linspace(-5, 5, 51)
x_t = np.sinc(t_axis)
X_f = abs(np.fft.fftshift(np.fft.fft(x_t)))


plt.figure('SignalDemo', figsize=(10,6), frameon=True)
plt.subplot(211)

markerline, stemlines, baseline = plt.stem(t_axis, x_t, markerfmt='.k', linefmt='k', basefmt='k', use_line_collection=True)
baseline.set_linewidth(1)

plt.title('x(t)')
plt.annotate(r'$\rightarrow dt \leftarrow$', xy=(0,0), xytext=(0.205, -0.1), textcoords='axes fraction')
plt.xticks([0, 1, 1.1, 5], ['0', '', '','T'])

plt.tick_params(left=False, labelleft=False)


plt.subplot(212)
markerline, stemlines, baseline = plt.stem(f_axis, X_f, markerfmt='.k', linefmt='k', basefmt='k', use_line_collection=True)
baseline.set_linewidth(1)

plt.title('X(f)')
plt.annotate(r'$\rightarrow df \leftarrow$', xy=(0,0), xytext=(0.205, -0.1), textcoords='axes fraction')
plt.xticks([-5, -3, -2.8, 0, 5], ['$-f_s/2$','', '', '0', '$f_s/2$'])
plt.tick_params(left=False, labelleft=False)

plt.show()
# plt.savefig('SignalDemo.png', dpi=400)
