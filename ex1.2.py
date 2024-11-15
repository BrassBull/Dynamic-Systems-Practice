import matplotlib.pyplot as plt
import math as math
import numpy as np
def H(n):
    if (n > 0):
        return (0.9875*H(n-1)+0.125)
    else:
        return (4)
def F(t_final, T):
    a = []
    for k in range(int(t_final/T)):
        a.append(H(k))
    return(a)
def r(t):
    return(10-6*math.e**(-t/20))
t = np.arange(0.,100.,0.001)
print(F(100,0.25))
plt.scatter(np.arange(0.,100.,0.25),F(100,0.25), s=10, color='red')
plt.plot(t, r(t))
plt.show()
