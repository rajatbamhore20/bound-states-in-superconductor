import numpy as np
import matplotlib.pyplot as plt

t = int(input())
del0 = float(input())

def eigen(E, del0, sign):
    tmp = (E**2 + del0**2)**0.5
    if sign == 1:
        return tmp
    return -tmp
def s_wave_band_structure(t, del0):
    x = np.linspace(0, np.pi, 100)
    y = np.linspace(np.pi, 2 * np.pi, 100)
    z = np.linspace(2 * np.pi, 3 * np.pi, 100)
    Ex = -2 * t * (1 + np.cos(x))
    Ey = -2 * t * (-1 + np.cos(y - np.pi))
    Ez = -4 * t * np.cos(z - 3 * np.pi)
    ax = plt.subplot()
    plt.plot(x, eigen(Ex, del0, 1), label = "$k_x+$")
    plt.plot(x, eigen(Ex, del0, 0), label = "$k_x-$")
    plt.plot(y, eigen(Ey, del0, 1), label="$k_y+$")
    plt.plot(y, eigen(Ey, del0, 0), label = "$k_y-$")
    plt.plot(z, eigen(Ez, del0, 1), label="$k_z+$")
    plt.plot(z, eigen(Ez, del0, 0), label = "$k_z-$")
    plt.legend(fontsize = 8)
    plt.axhline(0, color='black', linewidth=1)
    plt.title("Homogeneous S-wave State Band Structure")
    plt.xlabel("k-path")
    plt.ylabel("$Energy(E_k)$")
    labels = ["Γ", "X", 'M', "Γ"]
    tmp = [np.pi * i for i in range(4)]
    ax.set_xticks(tmp, labels)
    plt.show()
    return
def d_wave_band_structure(t, del0):
    x = np.linspace(0, np.pi, 100)
    y = np.linspace(np.pi, 2 * np.pi, 100)
    z = np.linspace(2 * np.pi, 3 * np.pi, 100)
    Ex = -2 * t * (1 + np.cos(x))
    Ey = -2 * t * (-1 + np.cos(y - np.pi))
    Ez = -4 * t * np.cos(z - 3 * np.pi)
    ax = plt.subplot()
    tmp = del0*2*(np.cos(x) - 1)
    plt.plot(x, eigen(Ex, tmp, 1), label="$k_x+$")
    plt.plot(x, eigen(Ex, tmp, 0), label="$k_x-$")
    tmp = del0*2*(-1 - np.cos(y - np.pi))
    plt.plot(y, eigen(Ey, tmp, 1), label="$k_y+$")
    plt.plot(y, eigen(Ey, tmp, 0), label="$k_y-$")
    tmp = 0
    plt.plot(z, eigen(Ez, tmp, 1), label="$k_z+$")
    plt.plot(z, eigen(Ez, tmp, 0), label="$k_z-$")
    plt.legend(fontsize=8)
    plt.axhline(0, color='black', linewidth=1)
    plt.title("Homogeneous D-wave State Band Structure")
    plt.xlabel("k-path")
    plt.ylabel("$Energy(E_k)$")
    labels = ["Γ", "X", 'M', "Γ"]
    tmp = [np.pi * i for i in range(4)]
    ax.set_xticks(tmp, labels)
    plt.show()
    return

def Energy(t, x, y, mu):
    return -2*t*(np.cos(x) + np.cos(y)) - mu

def Energyk(t, x, y, mu, f, del0):
    if f == "D":
        del0 *= 2*(np.cos(x) - np.cos(y))
    return (Energy(t, x, y, mu)**2 + del0**2)**0.5

ita = 5*10**(-2)
def plot_ldos(t, ita, f, del0):
    x = np.linspace(-5, 5, 5000)
    kx = np.linspace(-np.pi, np.pi, 100)
    ky = np.linspace(-np.pi, np.pi, 100)
    y = []
    for i in x:
        greens = 0
        for j in kx:
            for k in ky:
                greens += np.imag((0.5*(1 + Energy(t, j, k, 0)/Energyk(t, j, k, 0, f, del0)))/(i - Energyk(t, j, k, 0, f, del0) + ita*1j) + (0.5*(1 - Energy(t, j, k, 0)/Energyk(t, j, k, 0, f, del0)))/(i + Energyk(t, j, k, 0, f, del0) + ita*1j))
        y.append(-(1/np.pi)*greens)
        print(i)
    plt.plot(x, y)
    plt.title("Homogeneous " + f + "-wave LDOS")
    plt.ylabel("N(E)")
    plt.xlabel("$Energy(E)$")
    plt.show()
    return


s_wave_band_structure(t, del0)
d_wave_band_structure(t, del0)
plot_ldos(t, ita, "S", del0)
plot_ldos(t, ita, "D", del0)