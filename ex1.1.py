import matplotlib.pyplot as plt
import math as math
import numpy as np
def y(n, T):
    if (n>0):
        return ((1-2*T)*y(n-1,T)+3*n*T*T)
    else:
        return (1)
def r(x):
    return(1.75*math.e**(-2*x)+1.5*x-0.75)
def F(t_final, T):
    a = []
    for k in range(int(t_final/T)):
        a.append(y(k,T))
    return(a)
t = np.arange(0.,2.,0.001)
plt.scatter(np.arange(0.,2.,0.01),F(2,0.01), s=10)
plt.scatter(np.arange(0.,2.,0.025),F(2,0.025), s=10)
plt.scatter(np.arange(0.,2.,0.05),F(2,0.05), s=10)
plt.scatter(np.arange(0.,2.,0.1),F(2,0.1), s=10)
plt.plot(t, r(t))
plt.show()
