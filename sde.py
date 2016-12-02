#%%

import numpy
import matplotlib.pyplot as plt
import scipy
import scipy.stats

dt = 0.01
a = 1.0

ts = numpy.logspace(-1.0, 1.0, 10)

N = 5000

outs1 = numpy.zeros((N, len(ts)))
outs2 = numpy.zeros((N, len(ts)))
outs3 = numpy.zeros((N, len(ts)))

for n in range(N):
    t = 0.0
    r1 = 1.0
    r3 = 1.0
    x = numpy.array([1.0, 0.0, 0.0])
    b = numpy.array([1.0, 0.0, 0.0])
    #b = numpy.array([0.0])

    ti = 0
    nextt = ts[ti]

    while t < nextt:
        #dBt = numpy.random.randn(3) * numpy.sqrt(dt)

        dBt = numpy.sqrt(2 * a) * numpy.random.randn() * numpy.sqrt(dt)
        r1 = abs(r1 + (2 * a / r1) * dt + dBt)

        dBt = numpy.sqrt(2 * a) * numpy.random.randn(3) * numpy.sqrt(dt)
        r3 = abs(r3 + (2 * a / r3) * dt + b.dot(dBt) / r3)
        b += dBt

        dBt = numpy.sqrt(2 * a) * numpy.random.randn(3) * numpy.sqrt(dt)
        x += dBt

        r2 = numpy.linalg.norm(x)

        if t + dt > nextt:
            outs1[n, ti] = r1
            outs2[n, ti] = r2
            outs3[n, ti] = r3

            ti += 1

            if ti >= len(ts):
                break
            else:
                nextt = ts[ti]

        t += dt

    print n
#%%
x = numpy.linspace(-5.0, 5.0, 100)

labels = []

for tt, t in enumerate(ts):
    _, bins, _ = plt.hist(outs3[:, tt][outs3[:, tt] < 20], bins = 25, alpha = 0.5, color = 'r')
    plt.hist(outs2[:, tt], bins = bins, alpha = 0.5, color = 'g')
    plt.hist(outs1[:, tt], bins = bins, alpha = 0.5, color = 'b')
    print bins
    plt.xlim([0, 10.0])
    #m, s = scipy.stats.norm.fit(outs[:, tt])

    print m, s

    #plt.plot(x, scipy.stats.norm.pdf(x, m, s))

    labels.append("t = {0:0.2f}".format(ts[tt]))

    #plt.hist(outs[:, tt])
    #plt.title()
    #plt.
    plt.show()
plt.legend(labels, loc="upper left", bbox_to_anchor=(1,1))
plt.show()