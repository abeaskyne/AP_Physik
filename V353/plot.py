import matplotlib.pyplot as plt
import numpy as np
from scipy.optimize import curve_fit

t, u = np.genfromtxt("data.txt", unpack = True)
t = t*10**(-3)
x_log = np.linspace(0, 7*10**(-3), 1000)
params_log, cov_log = np.polyfit(t, np.log(u/3.6), deg = 1, cov = True)
errors_log = np.sqrt(np.diag(cov_log))

for name, value, error in zip("ab", params_log, errors_log):
    print("T2:"f"{name} = {value:.3f} ± {error:.3f}")


fig, ax =plt.subplots(1, 1, layout="constrained")
ax.plot(t, np.log(u/3.6), "k.")
ax.plot(x_log, params_log[0] * x_log + params_log[1])
ax.set_yscale("linear")
ax.set_ylabel((r'$log(\frac{U_c}{U_0})$'))
ax.set_xlabel(r'$t$ / s')

fig.savefig("plot1.pdf")

#-------------------------------------------------------------------------------------

A, F = np.genfromtxt("data1.txt", unpack = True)
A = A/3.6
x_log = np.linspace(0, 22000, 10000)
def f(x, a):
    return 1/(np.sqrt((1+(x*2*np.pi)**2)*a**2))
def w(x):
    return 1/(np.sqrt((1+(x*2*np.pi)**2)*0.00178**2))

params_log, cov_log = curve_fit(f, F, A, p0 = (0.003))
errors_log = np.sqrt(np.diag(cov_log))

for name, value, error in zip("ab", params_log, errors_log):
    print(":"f"{name} = {value:.5f} ± {error:.5f}")


fig, ax =plt.subplots(1, 1, layout="constrained")
ax.plot(F, A, "k.")
ax.plot(x_log, f(x_log, *params_log), label = "Fit der Messdaten" )
ax.plot(x_log, w(x_log), label = "Funktion mit RC = 0.00178")
ax.legend(loc = "best")
ax.set_xscale("log")
ax.set_yscale("linear")
ax.set_ylim(0,4)
ax.set_ylabel((r'$Relativmplitude$'))
ax.set_xlabel(r'$F / Hz')

fig.savefig("plot2.pdf")


T, F = np.genfromtxt("data2.txt", unpack = True)
x_log = np.linspace(0, 22000, 10000)
def f(x):
    return np.arctan(0.00178*x*2*np.pi)
def g(x):
    return np.arctan(0.00155*x*2*np.pi)

for name, value, error in zip("ab", params_log, errors_log):
    print(":"f"{name} = {value:.5f} ± {error:.5f}")





fig, ax =plt.subplots(1, 1, layout="constrained")
ax.plot(F, T, "k.", label = "Messwerte")
ax.plot(x_log, f(x_log), label = "Graph mit RC = 0.00178")
ax.plot(x_log, g(x_log), label = "Graph mit RC = 0.00155")
ax.set_xscale("log")
ax.set_yscale("linear")
ax.set_ylabel((r'$Phasenverschiebung$'))
ax.set_xlabel(r'$F / Hz')
ax.legend(loc = "best")

fig.savefig("plot3.pdf")

T, A = np.genfromtxt("data3.txt", unpack = True)
A = A/3.6
r = np.linspace(0.1, np.pi/2, 1000)

def f(x):
    return np.sin(x)/np.tan(x)



fig, ax = plt.subplots(subplot_kw = {"projection":"polar"})
ax.plot(A,T, "k.", label = "Messwerte")

ax.plot(f(r), r, label = "eigentliche Funktion")
ax.legend(loc = "best")


fig.savefig("plot4.pdf")




