import numpy as np
import matplotlib.pyplot as plt


f1 = 4
f2 = 15
f3 = 42
f4 = 67
fs = 1000
t = np.linspace(0,1,fs)
x = np.sin(2*np.pi*f1*t) + 2 * np.cos(2*np.pi*f2*t) + 1.5 * np.sin(2*np.pi*f3*t) + 0.5 * np.cos(2*np.pi*f4*t)

X = np.zeros(fs, dtype=complex)
for w in range(fs):
    for n in range(fs):
        X[w] += x[n] * np.exp(-2j * np.pi * n * w / fs)


fig, axs = plt.subplots(1,2, figsize=(10,5))
    
axs[0].plot(t, x)
axs[1].stem(np.abs(X))
axs[1].set_xlim([0, 100])

plt.savefig("ex3.pdf")
plt.show()