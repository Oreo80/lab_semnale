import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

f = 4
fs = 1000
t = np.linspace(0,1,fs)

x = np.sin(2*np.pi*f*t)
y = x * np.exp(-2j * np.pi * t)
fig, axs = plt.subplots(1,2, figsize=(10,5))

axs[0].plot(t,x)
axs[0].axhline(0, color='gray', linewidth=0.6)

axs[1].scatter(y.real, y.imag, c=np.abs(y))
axs[1].axhline(0, color='gray', linewidth=0.6)
axs[1].axvline(0, color='gray', linewidth=0.6)  
plt.savefig("ex2_a.pdf")
plt.show()

z1 = x * np.exp(-2j * np.pi * t * 1)
z2 = x * np.exp(-2j * np.pi * t * 3)
z3 = x * np.exp(-2j * np.pi * t * 4)
z4 = x * np.exp(-2j * np.pi * t * 8)

fig, axs = plt.subplots(2,2, figsize=(8,8))
for ax in axs.flat:
    ax.axhline(0, color='gray', linewidth=0.6)
    ax.axvline(0, color='gray', linewidth=0.6)
    ax.set_xlim([-1.1, 1.1])
    ax.set_ylim([-1.1, 1.1])
axs[0][0].scatter(z1.real, z1.imag, c=np.abs(z1))
axs[0][1].scatter(z2.real, z2.imag, c=np.abs(z2))
axs[1][0].scatter(z3.real, z3.imag, c=np.abs(z3))
axs[1][1].scatter(z4.real, z4.imag, c=np.abs(z4))

plt.savefig("ex2_b.pdf")
plt.show()


step = 10

# anim 1

fig, axs = plt.subplots(1, 2, figsize=(10, 5))

axs[0].set_xlim(0, 1)
axs[0].set_ylim(-1.1, 1.1)
axs[0].axhline(0, color='gray', linewidth=0.6)
linie = axs[0].plot([], [])[0]
punct = axs[0].scatter([], [], c='red')

axs[1].set_xlim(-1.1, 1.1)
axs[1].set_ylim(-1.1, 1.1)
axs[1].axhline(0, color='gray', linewidth=0.6)
axs[1].axvline(0, color='gray', linewidth=0.6)
linie_c = axs[1].scatter([], [], c=[], vmin=0, vmax=np.abs(y).max())
punct_c = axs[1].scatter([], [], c='red')

def update1(i):
    linie.set_data(t[:i], x[:i])
    punct.set_offsets([[t[i], x[i]]])
    linie_c.set_offsets(np.column_stack([y.real[:i], y.imag[:i]]))
    linie_c.set_array(np.abs(y[:i]))
    punct_c.set_offsets([[y.real[i], y.imag[i]]])
    return linie, punct, linie_c, punct_c

ani1 = FuncAnimation(fig, update1, frames=range(0, fs, step), interval=20, blit=True)
plt.show()

# anim 2

z = [z1, z2, z3, z4]
linii_c = []
puncte = []

fig, axs = plt.subplots(2, 2, figsize=(8,8))
axs = axs.flat
for i in range(4):
    axs[i].set_xlim(-1.1, 1.1)
    axs[i].set_ylim(-1.1, 1.1)
    axs[i].axhline(0, color='gray', linewidth=0.6)
    axs[i].axvline(0, color='gray', linewidth=0.6)
    linii_c.append(axs[i].scatter([], [], c=[], vmin=0, vmax=np.abs(z[i]).max()))
    puncte.append(axs[i].scatter([], [], c='red'))

def update2(i):
    for j in range(4):
        linii_c[j].set_offsets(np.column_stack([z[j].real[:i], z[j].imag[:i]]))
        linii_c[j].set_array(np.abs(z[j][:i]))
        puncte[j].set_offsets([[z[j].real[i], z[j].imag[i]]])
    return linii_c + puncte

ani2 = FuncAnimation(fig, update2, frames=range(0, fs, step), interval=20, blit=True)
plt.show()