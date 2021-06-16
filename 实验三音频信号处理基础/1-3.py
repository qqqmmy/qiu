from thinkdsp import read_wave
import matplotlib.pyplot as plt
from IPython.display import Audio
from thinkdsp import CosSignal,SinSignal
from thinkdsp import decorate

cos_sig = CosSignal(freq=440, amp=1.0, offset=0)
sin_sig = SinSignal(freq=880, amp=0.5, offset=0)


plt.subplot(3,2,1)
cos_sig.plot()
decorate(xlabel='Time (s)')

plt.subplot(3,2,2)
sin_sig.plot()
decorate(xlabel='Time (s)')


plt.subplot(3,2,3)
mix = sin_sig + cos_sig
mix.plot()
decorate(xlabel='Time (s)')


wave = mix.make_wave(duration=0.5, start=0, framerate=11025)
audio = Audio(data=wave.ys, rate=wave.framerate)
wave.make_audio()