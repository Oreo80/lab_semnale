import numpy as np
import matplotlib.pyplot as plt
from scipy.io import wavfile

fs, semnal = wavfile.read('untitled.wav')
N = len(semnal)
n = int(0.01*N)
pas = int(0.5 * n)

grupuri = []
for i in range(0, N - n + 1, pas):
    grup = semnal[i:i+n]
    grupuri.append(grup)

ffturi = []
for grup in grupuri:
    ffturi.append(np.abs(np.fft.fft(grup)))

matrice = np.column_stack(ffturi)
matrice = matrice[:n // 2, :]

matrice_db = 10 * np.log10(matrice + 1e-10)
plt.figure(figsize=(10, 6))
plt.imshow(matrice_db, aspect='auto', origin='lower', cmap='magma')

plt.savefig('ex6.pdf')
plt.show()