import numpy as np
import matplotlib.pyplot as plt
from collections import defaultdict
import time

t = int(input())
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
    # for i in lst:
    #     print(*i)
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
eigen(10)