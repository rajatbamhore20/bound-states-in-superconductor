<<<<<<< HEAD
import random

=======
>>>>>>> 3ec502bf72505e939a8ec7be1f365cb63ee2804e
import numpy as np
import matplotlib.pyplot as plt
from collections import defaultdict
import time

t = int(input())
<<<<<<< HEAD
del0 = float(input())
=======
>>>>>>> 3ec502bf72505e939a8ec7be1f365cb63ee2804e
def eigen(n):
    lst = [[0 for i in range(n)] for j in range(n)]
    for i in range(n):
        lst[i][(i-1)%n] = t
        lst[(i-1)%n][i] = t
    for i in lst:
        print(*i)
    eig, _ = np.linalg.eig(lst)
    eig_k = []
    for i in range(n):
        k = (2*np.pi*i)/n
        eig_k.append(-2*t*np.cos(k))
    eig.sort()
    eig_k.sort()
    # print(eig)
    # print(eig_k)
    tmp = [i for i in range(n)]
    plt.plot(tmp, eig, label="real space")
    plt.plot(tmp, eig_k, label="k space")
    plt.legend()
    plt.show()
    return

def eigen_2d(n):
    lst = [[0 for i in range(n**2)] for j in range(n**2)]
    p = defaultdict(int)
    k = 0
    for i in range(n):
        for j in range(n):
            p[(i, j)] = k
            k += 1
    for i in range(n):
        for j in range(n):
            lst[p[(i, j)]][p[((i-1)%n, j)]] = t
            lst[p[(i, j)]][p[(i+1)%n, j]] = t
            lst[p[(i, j)]][p[(i, (j-1)%n)]] = t
            lst[p[(i, j)]][p[(i, (j+1)%n)]] = t
<<<<<<< HEAD
    for i in lst:
        print(*i)
=======
    # for i in lst:
    #     print(*i)
>>>>>>> 3ec502bf72505e939a8ec7be1f365cb63ee2804e
    eig, _ = np.linalg.eig(lst)
    eig_k = []
    for i in range(n):
        kx = (2*np.pi*i)/(n)
        for j in range(n):
            ky = (2*np.pi*j)/(n)
            eig_k.append(2*t*(np.cos(kx)+np.cos(ky)))
    eig.sort()
    eig_k.sort()
    eig=[round(np.real(i),2) for i in eig]
    print(eig)
    eig_k=[round(i,2) for i in eig_k]
    print(eig_k)
    tmp = [i for i in range(n)]
    def hermiticity(arg,n):
        for i in range(n):
            for j in range(n):
                if arg[i][j]!=arg[j][i]:
                    return('no')
        return('yes')
    tmp = [i for i in range(n**2)]
    plt.plot(tmp, eig, label = "real space")
    plt.plot(tmp, eig_k, label = "k space")
    plt.legend()
    plt.show()
    print(hermiticity(lst,n**2))
    return
<<<<<<< HEAD
# eigen(10)
# eigen_2d(5)

def eigen_swave(n, imp):
    lst = [[0 for i in range(2*n**2)] for j in range(2*n**2)]
    p = defaultdict(int)
    k = 0
    tmp = n**2
    for i in range(n):
        for j in range(n):
            p[(i, j)] = k
            k += 1
    for i in range(n):
        for j in range(n):
            lst[p[(i, j)]][p[((i - 1) % n, j)]] = -t
            lst[p[(i, j)]][p[(i + 1) % n, j]] = -t
            lst[p[(i, j)]][p[(i, (j - 1) % n)]] = -t
            lst[p[(i, j)]][p[(i, (j + 1) % n)]] = -t
    for i in range(0, n**2):
        lst[i][i+n**2] = del0
    for i in range(n**2, 2*n**2):
        lst[i][i-n**2] = del0
    for i in range(n):
        for j in range(n):
            lst[tmp + p[(i, j)]][tmp + p[((i - 1) % n, j)]] = t
            lst[tmp + p[(i, j)]][tmp + p[(i + 1) % n, j]] = t
            lst[tmp + p[(i, j)]][tmp + p[(i, (j - 1) % n)]] = t
            lst[tmp + p[(i, j)]][tmp + p[(i, (j + 1) % n)]] = t
    def hermiticity(arg,n):
        for i in range(n):
            for j in range(n):
                if arg[i][j]!=arg[j][i]:
                    return('no')
        return('yes')
    # print(hermiticity(lst, n**2))
    # imp = random.uniform(0 ,8)
    tmp = 100
    lst[tmp][tmp] = imp
    lst[-tmp][-tmp] = imp
    eig, _ = np.linalg.eig(lst)
    eig = [round(np.real(i), 2) for i in eig]
    eig.sort()
    eigk = []
    for i in range(n):
        kx = (2*np.pi*i)/(n)
        for j in range(n):
            ky = (2*np.pi*j)/(n)
            E = -2*t*(np.cos(kx)+np.cos(ky))
            eigk.append(-(E**2 + del0**2)**0.5)
            eigk.append((E**2 + del0**2)**0.5)
    eigk = [round(i, 2) for i in eigk]
    eigk.sort()
    tmp = [i for i in range(2*n**2)]
    # print(eig)
    # plt.scatter(tmp, eig, label = "$real_space$", s = 1)
    # plt.scatter(tmp, eigk, label = "$k_space$", s = 1)
    # plt.ylabel("$EigenValue(E_{n})$")
    # plt.xlabel("index(n)")
    # plt.title("Inhomogeneous magnetic S-wave Superconductor Eigenvalues")
    # plt.legend()
    # plt.show()
    for i in eig:
        if i > -2 and i < 2:
            break
    if i > 2:
        return 2/del0
    return abs(i)/del0

# print(eigen_swave(50, 5))
tmp = np.arange(-20, 20, 1)
x = []
y = []
for i in tmp:
    k = eigen_swave(10, i)
    print(i, k)
    x.append(i)
    y.append(k)
plt.plot(x, y)
plt.ylabel("$|E_{b}|/∇$", fontsize = 12)
plt.xlabel("$V_{imp}$", fontsize = 12)
plt.title("S-wave magnetic impurity bound state energy eigenvalues", fontsize = 12)
plt.show()
=======
eigen(10)
>>>>>>> 3ec502bf72505e939a8ec7be1f365cb63ee2804e
