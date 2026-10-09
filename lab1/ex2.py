import numpy as np
import matplotlib.pyplot as plt


def sinus(f,t): return np.sin(2*np.pi*f*t)
def sawtooth(f, t): return np.mod(f*t, 1)
def square(f,t): return np.sign(sinus(f,t))

t = np.linspace(0,0.03,1600)
plt.figure()
plt.title("Sinus 400Hz")
plt.plot(t,sinus(400,t))
plt.savefig("ex2a.pdf")
plt.show()

#2b

t = np.linspace(0,3,100000)
plt.figure()
plt.title("Sinus 800Hz")
plt.plot(t,sinus(800,t))
plt.xlim(0, 0.03)
plt.savefig("ex2b.pdf")
plt.show()

#2c

t = np.linspace(0,0.03,1600)
plt.figure()
plt.title("Sawtooth 240Hz")
plt.plot(t,sawtooth(240,t))
plt.savefig("ex2c.pdf")
plt.show()

#2d

t = np.linspace(0,0.03,1600)
plt.figure()
plt.title("Square 300Hz")
plt.plot(t,square(300,t))
plt.savefig("ex2d.pdf")
plt.show()


#2e

# m = np.random.rand(128,128)
# m = np.random.uniform(size=(128,128))
m = np.random.normal(size=(128,128))
plt.figure()
plt.imshow(m)
plt.savefig("ex2e.pdf")
plt.show()

#2f

m = np.zeros((128,128))
m[30:70,20:30] = 1
m[60:70,20:60]=1
m[30:100,50:60]=1

m[30:40,70:110]=1
m[30:70,100:110]=1
m[60:70,70:110]=1
m[60:100,70:80]=1
m[90:100,70:110]=1
plt.figure()
plt.imshow(m)
plt.savefig("ex2f.pdf")
plt.show()