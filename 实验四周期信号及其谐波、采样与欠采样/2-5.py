from thinkdsp import Spectrum, TriangleSignal,SquareSignal,SawtoothSignal
from thinkdsp import decorate
import matplotlib.pyplot as plt
import numpy as np

def f5(spectrum):
    spectrum.hs[0]=0
    for i in range(1,len(spectrum.fs)):
        spectrum.hs[i]/=spectrum.fs[i]
    return spectrum

signal = SquareSignal(1100)#方波验证
duration = signal.period*4
segment = signal.make_wave(duration, framerate=10000)
wave = signal.make_wave(duration=1, framerate=10000)
spectrum = wave.make_spectrum()
plt.subplot(3,2,1)
spectrum.plot()
decorate(xlabel='Frequency (Hz)')

wave.apodize()
wave.make_audio()

spectrum = f5(spectrum)
plt.subplot(3,2,2)
spectrum.plot()
decorate(xlabel='Frequency (Hz)')

wave = spectrum.make_wave()
wave.apodize()
wave.make_audio()

signal = TriangleSignal(1100) #三角波验证
duration = signal.period*4
segment = signal.make_wave(duration, framerate=10000)
wave = signal.make_wave(duration=1, framerate=10000)
spectrum = wave.make_spectrum()
plt.subplot(3,2,3)
spectrum.plot()
decorate(xlabel='Frequency (Hz)')

wave.apodize()
wave.make_audio()

spectrum = f5(spectrum)
plt.subplot(3,2,4)
spectrum.plot()
decorate(xlabel='Frequency (Hz)')

wave = spectrum.make_wave()
wave.apodize()
wave.make_audio()

signal = SawtoothSignal(1100)#锯齿波验证
duration = signal.period*4
segment = signal.make_wave(duration, framerate=10000)
wave = signal.make_wave(duration=1, framerate=10000)
spectrum = wave.make_spectrum()
plt.subplot(3,2,5)
spectrum.plot()
decorate(xlabel='Frequency (Hz)')

wave.apodize()
wave.make_audio()

spectrum = f5(spectrum)
plt.subplot(3,2,6)
spectrum.plot()
decorate(xlabel='Frequency (Hz)')

wave = spectrum.make_wave()
wave.apodize()
wave.make_audio()

plt.show()