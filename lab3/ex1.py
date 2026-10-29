import numpy as np
import matplotlib.pyplot as plt

N = 8
F = np.zeros(shape = (N,N), dtype=complex)
# print(F)
for i in range(N):
    for k in range(N):
        F[i][k] = np.exp(-2j * np.pi * i * k / N)

# print(F)

fig, axs = plt.subplots(N, figsize=(10, 6))

for i in range(N):
    axs[i].plot(F[i].real)
    axs[i].plot(F[i].imag, "o--")

plt.savefig("ex1.pdf")
plt.show()

F_H = F.conj().T

unitara = np.allclose((F_H @ F) / N,np.eye(N))

print(unitara)