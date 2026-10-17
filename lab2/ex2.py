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

t = np.arange(0,0.03,1/fs)

plt.figure(figsize=(10,6))
plt.plot(t,sinus(1,100,t,0), label="0")
plt.plot(t,sinus(1,100,t,np.pi/2), label="pi/2")
plt.plot(t,sinus(1,100,t,np.pi/4), label="pi/4")
plt.plot(t,sinus(1,100,t,np.pi/6), label="pi/6")
plt.legend()
plt.grid()
plt.savefig("ex2a.pdf")
plt.show()


x = sinus(1,100,t,0)
z = np.random.normal(0,0.03,len(t))
snr = [0.1,1,10,100]
norm_x_sq = np.linalg.norm(x)**2
norm_z_sq = np.linalg.norm(z)**2

fig,axs = plt.subplots(2,2,figsize=(12,6))
axs = axs.flatten()
for i, snr in enumerate(snr):
    gamma = np.sqrt(norm_x_sq / (snr * norm_z_sq))
    semnal = x + gamma * z
    axs[i].plot(t,semnal)
    axs[i].grid(True)
    axs[i].set_title(f"snr = {snr}")

plt.tight_layout()
plt.savefig("ex2b.pdf")
plt.show()
