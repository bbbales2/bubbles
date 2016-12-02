#%%

import numpy
import matplotlib.pyplot as plt

N = 50
a = 1.0

rs = numpy.linspace(0, 1, N)

dr = rs[1] - rs[0]

u = numpy.zeros(N)
u[5] = 1

dt = 0.00010

T = 0.1

t = 0.0
it = 0

while t <= T:
    ou = u.copy()

    fp1h = 2 * a * (ou[2] + ou[1]) / (rs[2] + rs[1]) - a * (ou[2] - ou[1]) / dr
    u[1] = ou[1] - dt * (fp1h) / dr

    for i in range(2, N - 1):
        fm1h = 2 * a * (ou[i] + ou[i - 1]) / (rs[i] + rs[i - 1]) - a * (ou[i] - ou[i - 1]) / dr
        fp1h = 2 * a * (ou[i + 1] + ou[i]) / (rs[i + 1] + rs[i]) - a * (ou[i + 1] - ou[i]) / dr

        u[i] = ou[i] - dt * (fp1h - fm1h) / dr

    fm1h = 2 * a * (ou[N - 1] + ou[N - 2]) / (rs[N - 1] + rs[N - 2]) - a * (ou[N - 1] - ou[N - 2]) / dr

    u[N - 1] = ou[N - 1] - dt * (-fm1h) / dr


    t += dt
    it += 1

    if it % 10 == 0:
        total = 0.0
        for i in range(N):
            total += u[i]

        print total

        plt.plot(rs, u)
        plt.ylim((0, 0.2))
        plt.xlim((min(rs), max(rs)))
        plt.title("{0}".format(it))
        plt.show()

total = 0.0
for i in range(N):
    total += u[i]# * rs[i]**2

print total