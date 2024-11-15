import matplotlib.pyplot as plt
import math as math
import numpy as np
def y(n):
    if n > 0:
        return((1+0.00000000125*(25000000-y(n-1)))*y(n-1))
    else:
        return(3000000)
def F(n):
    a = []
    for k in range(0,n,10):
        a.append(y(k))
    return(a)

t = np.arange(0,100,25)
r = np.arange(0,51,1)
#plt.scatter(t,F(31), s=10, edgecolors='black')
for p in range(50):
    plt.scatter(t, (25-25*p/(p+(25-p)*math.e**(-0.00125*25*t)))*1.25*10**(-6))
#plt.plot(r, 0.00125*(25-r))
plt.show()