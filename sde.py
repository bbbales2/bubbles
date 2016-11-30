#%%

import numpy
import matplotlib.pyplot as plt
import scipy
import scipy.stats

dt = 0.01
a = 1.0

ts = numpy.logspace(-1.0, 1.0, 10)

N = 250

outs = numpy.zeros((N, len(ts)))

for n in range(N):
    t = 0.0
    r = 1.0
    b = numpy.array([0.0, 0.0, 0.0])
    #b = numpy.array([0.0])

    ti = 0
    nextt = ts[ti]

    while t < nextt:
        r = r + (numpy.sqrt(2 * a) / r) * dt
        
        #dBt = numpy.random.randn(3) * numpy.sqrt(dt)
        
        dBt = numpy.random.randn(3) * numpy.sqrt(dt)
        r = abs(r + numpy.sqrt(2 * a) * b.dot(dBt) / r)
        
        #dBt = numpy.random.randn(1) * numpy.sqrt(dt)
        #r = abs(r + numpy.sqrt(2 * a) * dBt)
        
        b += dBt

        if t + dt > nextt:
            outs[n, ti] = r

            ti += 1

            if ti >= len(ts):
                break
            else:
                nextt = ts[ti]

        t += dt
#%%
x = numpy.linspace(-5.0, 5.0, 100)

labels = []

for tt, t in enumerate(ts):
    plt.hist(outs[:, tt])
    m, s = scipy.stats.norm.fit(outs[:, tt])

    print m, s

    #plt.plot(x, scipy.stats.norm.pdf(x, m, s))

    labels.append("t = {0:0.2f}".format(ts[tt]))

    #plt.hist(outs[:, tt])
    #plt.title()
    #plt.
    plt.show()
plt.legend(labels, loc="upper left", bbox_to_anchor=(1,1))
plt.show()