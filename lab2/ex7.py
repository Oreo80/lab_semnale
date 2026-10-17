import numpy as np
import matplotlib.pyplot as plt
import scipy.io.wavfile as wavfile
import scipy.signal as signal
import sounddevice as sd

def sinus(A,f,t,b): return A * np.sin(2*np.pi*f*t + b)

fs = 1000
t = np.arange(0, 0.1, 1/fs)
f = 25

x = sinus(1,f,t,0)

xdec = x[::4]
tdec = t[::4]

xdecc = x[1::4]
tdecc = t[1::4]

fig, axs = plt.subplots(3,figsize=(10,6))
axs[0].stem(t,x)
axs[0].grid(True)
axs[1].stem(tdec,xdec)
axs[1].grid(True)
axs[2].stem(tdecc,xdecc)
axs[2].grid(True)

plt.savefig("ex7.pdf")
plt.show()


# a) dupa decimare, fs devine 250hz, forma undei se pastreaza
# b) decimarea cu offset 1 produce un semnal defazat fata de cel de la a), cu aceasi forma de unda