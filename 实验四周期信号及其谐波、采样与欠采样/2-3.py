from thinkdsp import TriangleSignal
from thinkdsp import decorate
import matplotlib.pyplot as plt
import numpy as np
from thinkdsp import SquareSignal

signal = SquareSignal(1100)#绘制1100Hz方波信号
duration = signal.period*3
segment = signal.make_wave(duration, framerate=10000)
plt.subplot(2,1,1)
segment.plot()
decorate(xlabel='Time (s)')

segment = signal.make_wave(duration=0.5, framerate=10000)
spectrum = segment.make_spectrum()
plt.subplot(2,1,2)
spectrum.plot()
decorate(xlabel='Frequency (Hz)')
plt.show()
