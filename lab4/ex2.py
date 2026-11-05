import numpy as np
import matplotlib.pyplot as plt

f0 = 8
fs = 10

f1 = f0 + fs
f2 = f0 + 2*fs

t = np.linspace(0,1,1000)
n = np.arange(0, 1, 1/fs)

f = [f0,f1,f2]

fig,axs = plt.subplots(3, figsize = (10,6))

x = lambda f,t: np.sin(2*np.pi*f*t)

for i in range(3):
    axs[i].plot(t,x(f[i],t))
    axs[i].stem(n,x(f[i],n), markerfmt = 'r', linefmt='r')
    axs[i].set_title(f"{f[i]} Hz")
    axs[i].grid(True)

plt.tight_layout()
plt.savefig("ex2.pdf")
plt.show()
