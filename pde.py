#%%

import numpy
import matplotlib.pyplot as plt

N = 50
a = 1.0

#rs = 1.0 / numpy.linspace(0, 1, N)

V = 1.0

rs = numpy.zeros(N)
rs[1] = 1.0

for i in range(2, N):
    vp = rs[i - 1]**3 - rs[i - 2]**3
    
    rs[i] = numpy.power(2 * rs[i - 1]**3 - rs[i - 2]**3, 1.0 / 3.0)
    #rs[i] = i**3 - rs[i - 1]
    
rs /= numpy.max(rs)

#%%

dr = rs[1] - rs[0]

u = numpy.zeros(N)
u[5] = 10

dt = 0.001

T = 1.0

t = 0.0
it = 0

while t <= T:
    ou = u.copy()
        
    rp1h = (rs[1] + rs[0]) / 2
    fp1h = a * rp1h**2 * (ou[1] - ou[0]) / dr
    u[0] = ou[0] + 3 * dt * (fp1h) / (rp1h**3)
    
    #print fp1h

    for i in range(1, N - 1):
        rm1h = (rs[i] + rs[i - 1]) / 2
        rp1h = (rs[i + 1] + rs[i]) / 2
        
        fm1h = a * rm1h**2 * (ou[i] - ou[i - 1]) / dr
        fp1h = a * rp1h**2 * (ou[i + 1] - ou[i]) / dr
        
        #if i == 1:
        #    print fm1h
        
        u[i] = ou[i] + 3 * dt * (fp1h - fm1h) / (rp1h**3 - rm1h**3)
        
    rm1h = (rs[N - 1] + rs[N - 2]) / 2
    
    fm1h = a * rm1h**2 * (ou[N - 1] - ou[N - 2]) / dr
        
    u[N - 1] = ou[i] + 3 * dt * (-fm1h) / ((rm1h + dr / 2.0)**3 - rm1h**3)
    
    
    t += dt
    it += 1
    
    if it % 10 == 0:
        total = 0.0
        for i in range(N):
            total += u[i] * rs[i]**2
            
        print total
        
        plt.plot(rs, u)
        plt.ylim((0, 10.0))
        plt.xlim((min(rs), max(rs)))
        plt.title("{0}".format(it))
        plt.show()