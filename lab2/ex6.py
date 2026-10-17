import numpy as np
import matplotlib.pyplot as plt
import scipy.io.wavfile as wavfile
import scipy.signal as signal
import sounddevice as sd

def sinus(A,f,t,b): return A * np.sin(2*np.pi*f*t + b)

fs = 1000
t = np.arange(0, 3, 1/fs)

a = sinus(1,fs/2,t,0)
b = sinus(1,fs/4,t,0)
c = sinus(1,0,t,0)

fig,axs = plt.subplots(3)

axs = axs.flatten()

for i in range(len(axs)):
    axs[i].set_xlim(0,0.03)
    axs[i].grid(True)
axs[0].plot(t,a)
axs[1].plot(t,b)
axs[2].plot(t,c)

plt.savefig("ex6.pdf")
plt.show()

# semnalul cu 0hz e semnal nul, in orice moment e 0
# semnalul cu fs/2 apare nul pe grafic deoarece din formula matematica a semnalului discret avem sin(2pi * fs/2 * n/fs) = sin(pi*n) care e 0, practic mereu esantionam atunci cand semnalul e 0