import numpy as np
import matplotlib.pyplot as plt
import scipy.io.wavfile as wavfile
import scipy.signal as signal
import sounddevice as sd

def sinus(f,t): return np.sin(2*np.pi*f*t)
def sawtooth(f, t): return np.mod(f*t, 1)

fs = 44100
t = np.arange(0, 3, 1/fs)

a = sinus(400,t)
c = sawtooth(400,t)

fig, axs = plt.subplots(3)
axs = axs.flatten()
for i in range(len(axs)):
    axs[i].set_xlim(0,0.03)
axs[0].plot(t,a)
axs[1].plot(t,c)
axs[2].plot(t,a+c)
plt.savefig("ex4.pdf")
plt.show()

sd.play(a+c,fs)
sd.wait()