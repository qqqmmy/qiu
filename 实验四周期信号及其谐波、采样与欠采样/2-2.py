from thinkdsp import TriangleSignal
from thinkdsp import decorate
import matplotlib.pyplot as plt
import numpy as np

signal = TriangleSignal(200) #绘制三角波
duration = signal.period*3
segment = signal.make_wave(duration, framerate=10000)
plt.subplot(3,2,1)
segment.plot()
decorate(xlabel='Time (s)')

wave = signal.make_wave(duration=0.5, framerate=10000)
wave.apodize()
wave.make_audio()

spectrum = wave.make_spectrum()#绘制三角波频谱
plt.subplot(3,2,2)
spectrum.plot()
decorate(xlabel='Frequency (Hz)')

from thinkdsp import SquareSignal

signal = SquareSignal(200)#绘制方波
duration = signal.period*3
segment = signal.make_wave(duration, framerate=10000)
plt.subplot(3,2,3)
segment.plot()
decorate(xlabel='Time (s)')

wave = signal.make_wave(duration=0.5, framerate=10000)
wave.apodize()
wave.make_audio()

spectrum = wave.make_spectrum()#绘制方波频谱
plt.subplot(3,2,4)
spectrum.plot()
decorate(xlabel='Frequency (Hz)')

from thinkdsp import SawtoothSignal

signal = SawtoothSignal(200)#绘制锯齿信号
duration = signal.period*3
segment = signal.make_wave(duration, framerate=10000)
plt.subplot(3,2,5)
segment.plot()
decorate(xlabel='Time (s)')

wave = signal.make_wave(duration=0.5, framerate=10000)
wave.apodize()
wave.make_audio()

spectrum = wave.make_spectrum()
plt.subplot(3,2,6)
spectrum.plot()
decorate(xlabel='Frequency (Hz)')

plt.show()