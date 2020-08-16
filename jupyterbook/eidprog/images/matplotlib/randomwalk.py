from math import pi

import numpy as np
from numpy.random import rand
import matplotlib.pyplot as plt


npts = 10000
r = 0.1
for i in range(3):
    richtung = 2*pi*rand(npts)
    dx = r*np.cos(richtung)
    dy = r*np.sin(richtung)

    x = [0]
    y = [0]
    for n in range(npts):
        x.append(x[-1]+dx[n])
        y.append(y[-1]+dy[n])
    plt.plot(x, y)

plt.xlabel("x")
plt.ylabel("y")
plt.savefig("randomwalk.png")
