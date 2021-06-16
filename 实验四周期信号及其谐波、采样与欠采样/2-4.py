from thinkdsp import Spectrum, TriangleSignal
from thinkdsp import decorate
import matplotlib.pyplot as plt
import numpy as np

signal = TriangleSignal(440) #绘制三角波
duration = signal.period*3
segment = signal.make_wave(duration, framerate=10000)
plt.subplot(3,1,1)
segment.plot()
decorate(xlabel='Time (s)')

wave = signal.make_wave(duration=0.01, framerate=10000)
plt.subplot(3,1,2)
Spectrum = wave.make_spectrum()
Spectrum.plot()
print(Spectrum.hs[0])
decorate(title=Spectrum.hs[0])

plt.subplot(3,1,3)
Spectrum.hs[0] = 100
Spectrum.plot()
decorate(title=Spectrum.hs[0])

plt.show()