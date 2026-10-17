import numpy as np
import matplotlib.pyplot as plt
import scipy.io.wavfile as wavfile
import scipy.signal as signal
import sounddevice as sd

def sinus(f,t): return np.sin(2*np.pi*f*t)

fs = 44100
t = np.arange(0, 3, 1/fs)

a = sinus(400,t)
c = sinus(700,t)

v = np.concatenate((a,c))

sd.play(v,fs)
sd.wait()

# semnalul cu frecventa mai mare se aude mai ascutit, are pitchul mai mare