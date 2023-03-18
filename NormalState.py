import numpy as np
import matplotlib.pyplot as plt
import time
print(time.time())

t = int(input())
ita = 5*10**(-2)
def band_structure(t):
    x = np.linspace(0, np.pi, 100)
    y = np.linspace(np.pi, 2*np.pi, 100)
    z = np.linspace(2*np.pi, 3*np.pi, 100)
    Ex = -2*t*(1 + np.cos(x))
    Ey = -2*t*(-1 + np.cos(y - np.pi))
    Ez = -4*t*np.cos(z - 3*np.pi)
    plt.figure(figsize=(10,7))
    ax = plt.subplot()
    plt.plot(x, Ex, label = "$k_x$")
    plt.plot(y, Ey, label = "$k_y$")
    plt.plot(z, Ez, label = "$k_z$")
    plt.legend(fontsize = 13)
    plt.title("Normal State Band Structure")
    plt.xlabel("k-path")
    plt.ylabel("$Energy(E_k)$")
    labels = ["Γ", "X", 'M', "Γ"]
    tmp = [np.pi*i for i in range(4)]
    ax.set_xticks(tmp, labels)
    plt.axhline(0, color='black', linewidth=1)
    plt.show()
    return

def fermi_surface(t):
    x = np.linspace(-np.pi, np.pi, 100)
    y = np.linspace(-np.pi, np.pi, 100)
    x, y = np.meshgrid(x, y)
    z = Energy(t, x, y, 0)
    cs = plt.contour(x, y, z)
    plt.clabel(cs, inline=True, fontsize=10)
    plt.title("Fermi Surface Contour")
    plt.xlabel("X")
    plt.ylabel("Y")
    plt.axhline(0, color='black')
    plt.axvline(0, color='black')
    plt.show()
    return

def Energy(t, x, y, mu):
    return -2*t*(np.cos(x) + np.cos(y)) - mu

def plot_ldos(t, ita):
    x = np.linspace(-5, 5, 1000)
    kx = np.linspace(-np.pi, np.pi, 100)
    ky = np.linspace(-np.pi, np.pi, 100)
    y = []
    for i in x:
        greens = 0
        for j in kx:
            for k in ky:
                greens += np.imag(1/(i - Energy(t, j, k, 0) + ita*1j))
        tmp = -(1/np.pi)*greens
        y.append(tmp)
        print(i)
    plt.plot(x, y)
    plt.title("Normal State Lattice LDOS")
    plt.ylabel("N(E)")
    plt.xlabel("$Energy(E)$")
    plt.show()
    return



# band_structure(t)
# fermi_surface(t)
plot_ldos(t, ita)

