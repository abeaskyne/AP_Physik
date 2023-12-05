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



