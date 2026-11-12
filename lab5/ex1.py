import numpy as np
import matplotlib.pyplot as plt
x = np.genfromtxt("Train.csv", delimiter=',', skip_header=1, usecols=2)
x_raw = x.copy()
# print(x.shape, x[:10])

'''
Exercitiul 1 a)

Enuntul ne zice ca nr. de masini care trec printr-o intersectie este masurat din ora in ora 
=> un esantion la 3600 secunde => ts = 3600 => fs = 1/3600 Hz

Exercitiul 1 b)
Avem 18288 esantioane, stim ca esantioanele sunt la o ora distanta, deci intervalul de timp este 18287 ore ~ 2.0875 ani

'''
N = len(x)
fs = 1/3600
ts = 3600
print(N) # 18288

'''
Exercitiul 1 c)

Semnal esantionat optim => toate frecventele sunt sub fs/2 => frecventa maxima e la limita
fmax = fs/2 = (1/3600)/2 = 1/7200  ~ 0.00013888888 Hz
'''

# Exercitiul 1 d)
X = np.fft.fft(x)
X = np.abs(X/N)
X = X[:N//2]
f = fs*np.linspace(0,N//2,N//2)/N

plt.figure()
markerline, stemlines, baseline = plt.stem(f, np.abs(X), linefmt='k-', basefmt='k-')
plt.setp(markerline, markerfacecolor='none', markeredgecolor='black', markersize=7)
plt.savefig("ex1d.pdf")
plt.show()

'''
Exercitiul 1 e)
Da, are componenta continua, media semnalului este 138.95, ea fiind componenta 0 din fft ar trebui sa fie centrata in jurul lui 0
'''

print(x.mean()) # ~ 138.95
x = x-np.mean(x)

X = np.fft.fft(x)
X = np.abs(X/N)
X = X[:N//2]

plt.figure()
markerline, stemlines, baseline = plt.stem(f, np.abs(X), linefmt='k-', basefmt='k-')
plt.setp(markerline, markerfacecolor='none', markeredgecolor='black', markersize=7)
plt.savefig("ex1e.pdf")
plt.show()

# Exercitiul 1 f)

v = np.argsort(X)[::-1][:4]
for i in v:
    T = 1/f[i]/3600
    print(f"X={X[i]}  f = {f[i]} Hz, {T}h")

# Exercitiul 1 g)

# o luna trafic => 30*24 = 720h
start = 9456
t = np.arange(start,start+720)
plt.figure(figsize=(12,6))
plt.plot(t,x_raw[start:start+720])
plt.savefig("ex1g.pdf")
plt.show()


'''
Exercitiul 1 h)

Semnalul se repeta zilnic si saptamanal
Pentru a deduce ora primului esantion putem suprapune zilele si vedem unde pica minimul de noapte, 
asumand ca traficul este mic noaptea si mare pe timp de zi

Pentru a deduce ziua primului esantion putem, in mod similar, sa suprapunem saptamanile, 
identificam weekendul ca fiind cele 2 zile de minim si putem deduce din asta ziua primului esantion

Ca sa deducem data exacta am avea nevoie de altceva, o zi de sarbatoare cunoscuta, zi libera, unde pot folosi data cunoscuta in prealabil

Neajunsuri: zgomotul muta minimul, schimbarea de ora, sarbatori mobile.
'''

# Exercitiul 1 i)
# taiem frecventele inalte, aleg sa nu permit un eveniment sa se repete mai mult de doua ori pe zi (permit aglomeratia de dimineata si cea de seara)
# k = 2*N/24 = 1524
X = np.fft.fft(x_raw)
k = 1524
X[k:N-k] = 0
x_filtered = np.fft.ifft(X).real

plt.figure(figsize=(12,6))
plt.plot(t, x_raw[start:start+720])
plt.plot(t, x_filtered[start:start+720])
plt.savefig("ex1i.pdf")
plt.show()