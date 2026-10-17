import numpy as np
import matplotlib.pyplot as plt
import scipy.io.wavfile as wavfile
import scipy.signal as signal
import sounddevice

# rate = int(10e5)
fs = 44100

# wavfile.write('',rate)
# sounddevice.play(array,fs)

def sinus(A,f,t,b): return A * np.sin(2*np.pi*f*t + b)
def cosinus(A,f,t,b): return A * np.cos(2*np.pi*f*t + b)

t = np.arange(0,0.03,1/fs)
# cos(t) = sin(t+ pi/2) = > sinus(1,100,tn,0) echivalent cu cosinus(1,100,tn,-np.pi/2)
fig, axs = plt.subplots(2)
axs[0].plot(t,sinus(1,100,t,0))
axs[0].set_title("sinus")
axs[0].grid(True)
axs[1].plot(t,cosinus(1,100,t,-np.pi/2))
axs[1].set_title("cosinus")
axs[1].grid(True)
plt.tight_layout()
plt.savefig("ex1.pdf")
plt.show()