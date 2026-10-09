import numpy as np
import matplotlib.pyplot as plt


def x(t): return np.cos(520*np.pi*t + np.pi/3)
def y(t): return np.cos(280*np.pi*t - np.pi/3)
def z(t): return np.cos(120*np.pi*t + np.pi/3)

t = np.arange(0,0.03,0.0005)

#b
fig, axs = plt.subplots(3)
fig.suptitle("Semnale")
axs[0].plot(t, x(t))
axs[1].plot(t,y(t))
axs[2].plot(t,z(t))
plt.tight_layout()
fig.savefig("ex1b.pdf")
plt.show()


#c
fs = 200
tn = np.arange(0,0.03,1/fs)

fig, axs = plt.subplots(3)
fig.suptitle("Semnale 200Hz")
axs[0].plot(t, x(t))
axs[1].plot(t,y(t))
axs[2].plot(t,z(t))
axs[0].stem(tn, x(tn))
axs[1].stem(tn,y(tn))
axs[2].stem(tn,z(tn))
plt.tight_layout()
fig.savefig("ex1c.pdf")
plt.show()