import numpy as np
import matplotlib.pyplot as plt
import time

def dft(x):
    N = len(x)
    n = np.arange(N)
    F = np.exp(-2j * np.pi * np.outer(n, n) / N)
    return F @ x

def fft(x):
    N = len(x)
    if N == 1:
        return x
    M = N//2
    w = np.exp(-2j * np.pi / N)
    k = np.arange(M)
    omega = w ** k
    z_t = fft(x[0::2])
    z_b = omega * fft(x[1::2])
    return np.concatenate([z_t + z_b, z_t - z_b])


Ns = [128, 256, 512, 1024, 2048, 4096, 8192]

dftt = []
fftmanualt = []
fftt = []

for N in Ns:
    x = np.random.rand(N)

    t = time.time()
    dft(x)
    dftt.append(time.time() - t)

    t = time.time()
    fft(x)
    fftmanualt.append(time.time() - t)

    t = time.time()
    np.fft.fft(x)
    fftt.append(time.time() - t)

plt.figure()
plt.plot(Ns,dftt, label="dft manual")
plt.plot(Ns,fftmanualt, label="fft manual")
plt.plot(Ns, fftt, label="fft")
plt.yscale("log")
plt.legend()
plt.grid()

plt.savefig("ex1.pdf")
plt.show()
