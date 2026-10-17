import numpy as np
import matplotlib.pyplot as plt
import scipy.io.wavfile as wavfile
import scipy.signal as signal
import sounddevice as sd

##### exercitiul 2 lab 1
def sinus(f,t): return np.sin(2*np.pi*f*t)
def sawtooth(f, t): return np.mod(f*t, 1)
def square(f,t): return np.sign(sinus(f,t))

# am modificat esantioanele la a si timpii la toti fata de lab 1 ca sa si aud ceva

fs = 44100
t = np.arange(0, 3, 1/fs)

# plt.figure()
# plt.title("Sinus 400Hz")
# plt.plot(t,sinus(400,t))
# plt.stem(t,sinus(400,t))
# plt.xlim(0, 0.003)
# plt.savefig("ex2a.pdf")
# plt.show()

a = sinus(400,t)

#2b

# plt.figure()
# plt.title("Sinus 800Hz")
# plt.plot(t,sinus(800,t))
# plt.xlim(0, 0.03)
# plt.savefig("ex2b.pdf")
# plt.show()

b = sinus(800,t)

#2c

# plt.figure()
# plt.title("Sawtooth 240Hz")
# plt.plot(t,sawtooth(240,t))
# plt.savefig("ex2c.pdf")
# plt.show()

c = sawtooth(240,t)

#2d

# plt.figure()
# plt.title("Square 300Hz")
# plt.plot(t,square(300,t))
# plt.savefig("ex2d.pdf")
# plt.show()

d = square(300,t)


#######

# rate = int(10e5)
# fs = 44100

# wavfile.write('',rate)
sd.play(a,fs)
sd.wait()
sd.play(b,fs)
sd.wait()
sd.play(c,fs)
sd.wait()
sd.play(d,fs)

# audio = np.concatenate((a,b,c,d))
# sd.play(d,fs)
# sd.wait()


wavfile.write('lab1_2b.wav',fs,b)
fs_disk, b_disk = wavfile.read('lab1_2b.wav')
sd.play(b_disk,fs_disk)
sd.wait()