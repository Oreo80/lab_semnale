import numpy as np
import matplotlib.pyplot as plt
import scipy.io.wavfile as wavfile
import scipy.signal as signal
import sounddevice as sd

alpha = np.linspace(-np.pi/2, np.pi/2, 1000)

sin_a = np.sin(alpha)
aprox = alpha
aprox_pade = (alpha - (7*alpha ** 3) / 60) / (1 + (alpha**2)/20)

err_t = np.abs(sin_a - aprox)
err_pade = np.abs(sin_a - aprox_pade)

fig, axs = plt.subplots(2,figsize=(10,6))
axs[0].plot(alpha, sin_a, label="sin")
axs[0].plot(alpha, aprox, label="aprox taylor")
axs[0].plot(alpha, aprox_pade, label="aprox pade")
axs[0].grid(True)
axs[0].legend()

axs[1].plot(alpha,err_t, label="eroare taylor")
axs[1].plot(alpha,err_pade, label="eroare pade")
axs[1].grid(True)
axs[1].legend()
axs[1].set_yscale('log')

plt.savefig("ex8.pdf")
plt.show()