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
        return 2
    return abs(i)

# print(eigen_swave(50, 5))
tmp = np.arange(-20, 20, 1)
x = []
y = []
for i in tmp:
    k = eigen_swave(30, i)
    print(i, k)
    x.append(i)
    y.append(k)
plt.plot(x, y)
plt.ylabel("$|E_{b}|/∇$", fontsize = 16)
plt.xlabel("$V_{imp}$", fontsize = 16)
plt.title("S-wave magnetic impurity bound state energy eigenvalues", fontsize = 16)
plt.show()
