import matplotlib.pyplot as plt
import numpy as np


B, r = np.genfromtxt("data1.txt", unpack = True)
r = r * 10**(-2)
x_log = np.linspace(0, 0.004, 1000)
params_log, cov_log = np.polyfit(B, r, deg = 1, cov = True)
errors_log = np.sqrt(np.diag(cov_log))

for name, value, error in zip("ab", params_log, errors_log):
    print("T2:"f"{name} = {value:.3f} ± {error:.3f}")


fig, ax =plt.subplots(1, 1, layout="constrained")
ax.plot(B, r , "k.")
ax.plot(x_log, params_log[0] * x_log + params_log[1])
ax.set_yscale("linear")
ax.set_ylabel((r'Abstand r/m'))
ax.set_xlabel(r'Magnetische Flussdichte B/T')

fig.savefig("plot1.pdf")


B, T = np.genfromtxt("data2.txt", unpack = True)
T
x_log = np.linspace(0, 14, 1000)
params_log, cov_log = np.polyfit(T**2, 1/B,deg = 1, cov = True)
errors_log = np.sqrt(np.diag(cov_log))

for name, value, error in zip("ab", params_log, errors_log):
    print("T2:"f"{name} = {value:.3f} ± {error:.3f}")


fig, ax =plt.subplots(1, 1, layout="constrained")
ax.plot(T**2, 1/B, "k.")
ax.plot(x_log, params_log[0] * x_log + params_log[1])
ax.set_yscale("linear")
ax.set_xlabel((r'T^2[s^2]'))
ax.set_ylabel(r'1/B[1/T]')

fig.savefig("plot2.pdf")

B, T = np.genfromtxt("data3.txt", unpack = True)

x_log = np.linspace(0, 0.005, 1000)
params_log, cov_log = np.polyfit(B, 1/T,deg = 1, cov = True)
errors_log = np.sqrt(np.diag(cov_log))

for name, value, error in zip("ab", params_log, errors_log):
    print("T2:"f"{name} = {value:.3f} ± {error:.3f}")


fig, ax =plt.subplots(1, 1, layout="constrained")
ax.plot(B, 1/T, "k.")
ax.plot(x_log, params_log[0] * x_log + params_log[1])
ax.set_yscale("linear")
ax.set_xlabel((r'B[T]'))
ax.set_ylabel(r'1/Tp[1/s]')

fig.savefig("plot3.pdf")







